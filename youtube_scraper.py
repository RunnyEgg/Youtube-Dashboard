import pandas as pd
from googleapiclient.discovery import build
from tqdm import tqdm

# Replace with your API key
API_KEY = 'your_api_key'
# Replace with the channel ID of the YouTube channel you want to scrape
CHANNEL_ID = 'channel_id'

def get_channel_videos(channel_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get channel details
    print("Fetching channel details...")
    channel_request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id
    )
    channel_response = channel_request.execute()

    # Extract channel details
    channel_info = channel_response['items'][0]['snippet']
    channel_statistics = channel_response['items'][0]['statistics']
    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Fetch all video details
    print("Fetching video details...")
    videos = []
    next_page_token = None

    total_videos = int(channel_statistics.get('videoCount', 0))

    with tqdm(total=total_videos, desc="Fetching videos") as pbar:
        while True:
            playlist_request = youtube.playlistItems().list(
                part='snippet',
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()

            for item in playlist_response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_request = youtube.videos().list(
                    part='snippet,statistics,contentDetails,status',
                    id=video_id
                )
                video_response = video_request.execute()
                video_data = video_response['items'][0]
                videos.append(video_data)
                pbar.update(1)

            next_page_token = playlist_response.get('nextPageToken')
            if next_page_token is None:
                break

    return channel_info, channel_statistics, videos


def main():
    channel_info, channel_statistics, videos = get_channel_videos(CHANNEL_ID, API_KEY)

    # Create a DataFrame for channel information
    channel_data = {
        'Title': channel_info['title'],
        'Description': channel_info['description'],
        'Published At': channel_info['publishedAt'],
        'Subscriber Count': channel_statistics.get('subscriberCount', 'N/A'),
        'View Count': channel_statistics.get('viewCount', 'N/A'),
        'Video Count': channel_statistics.get('videoCount', 'N/A'),
        'Country': channel_info.get('country', 'N/A'),
        'Custom URL': channel_info.get('customUrl', 'N/A'),
        'Default Language': channel_info.get('defaultLanguage', 'N/A'),
        'Banner Image URL': channel_info.get('thumbnails', {}).get('high', {}).get('url', 'N/A'),
        'Profile Image URL': channel_info.get('thumbnails', {}).get('default', {}).get('url', 'N/A')
    }
    channel_df = pd.DataFrame([channel_data])

    # Create a DataFrame for videos
    video_data = []
    for video in tqdm(videos, desc="Processing videos"):
        video_info = {
            'Title': video['snippet']['title'],
            'Description': video['snippet']['description'],
            'Published At': video['snippet']['publishedAt'],
            'View Count': video['statistics'].get('viewCount', 'N/A'),
            'Like Count': video['statistics'].get('likeCount', 'N/A'),
            'Comment Count': video['statistics'].get('commentCount', 'N/A'),
            'Tags': ", ".join(video['snippet'].get('tags', [])),
            'Duration': video['contentDetails'].get('duration', 'N/A'),
            'Category': video['snippet'].get('categoryId', 'N/A'),
            'Definition': video['contentDetails'].get('definition', 'N/A'),
            'Caption': video['contentDetails'].get('caption', 'N/A'),
            'License': video['contentDetails'].get('licensedContent', 'N/A'),
            'Recording Date': video['snippet'].get('recordingDetails', {}).get('recordingDate', 'N/A'),
            'Viewable Status': video.get('status', {}).get('privacyStatus', 'N/A'),
            'Video ID': video['id']
        }
        video_data.append(video_info)

    videos_df = pd.DataFrame(video_data)

    # Save to Excel
    print("Saving data to Excel...")
    with pd.ExcelWriter('youtube_channel_data.xlsx', engine='openpyxl') as writer:
        channel_df.to_excel(writer, sheet_name='Channel Info', index=False)
        videos_df.to_excel(writer, sheet_name='Videos', index=False)
    print("Data saved to youtube_channel_data.xlsx")


if __name__ == "__main__":
    main()
