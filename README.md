
# YouTube Channel Performance Dashboard

This project demonstrates my journey in data analysis, Python programming, and data visualization through the creation of a dashboard that highlights key performance metrics of a YouTube channel. The chosen channel for this analysis is Aliensrock, a favorite of mine.

## Table of Contents

- [Introduction](#introduction)
- [Project Motivation](#project-motivation)
- [Technologies Used](#technologies-used)
- [Project Steps](#project-steps)
  - [Data Collection](#data-collection)
  - [Data Processing](#data-processing)
  - [Data Visualization](#data-visualization)
- [Key Learnings](#key-learnings)
- [What I Would Like To Do In The Future](#what-i-would-like-to-do-in-the-future)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

The goal of this project was to create a comprehensive dashboard that effectively showcases important metrics and insights about a YouTube channel. Since I do not have my own YouTube channel, I chose Aliensrock due to my interest in their content.

## Project Motivation

I wanted to create a project that would showcase my skills in data analysis, incorporating my interests in a meaningful way. Creating a YouTube channel performance dashboard seemed like the perfect opportunity to do so, allowing me to explore various tools and techniques in the process.

## Technologies Used

- **Python**: For data scraping using the YouTube Data API v3.
- **YouTube Data API v3**: Provided by Google Cloud to fetch data about YouTube channels and their videos.
- **Pandas**: For data manipulation and analysis.
- **Excel**: For data storage and preliminary analysis.
- **Power BI**: For creating an interactive dashboard for data visualization.

## Project Steps

### Data Collection

I started with the idea of making a project that showcases some of my skills. To gather data from YouTube, I wrote a Python script that uses the YouTube Data API v3. This script fetches channel details, statistics, and video information. The script retrieves data such as view count, likes, comments, video titles, and more. Here is a brief snippet of the script:

```python
import pandas as pd
from googleapiclient.discovery import build
from tqdm import tqdm

API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'UCeP4Yv3s4RvS0-6d9OInRMw'

def get_channel_videos(channel_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_request = youtube.channels().list(part='snippet,contentDetails,statistics', id=channel_id)
    channel_response = channel_request.execute()
    ...
    return channel_info, channel_statistics, videos

def main():
    channel_info, channel_statistics, videos = get_channel_videos(CHANNEL_ID, API_KEY)
    ...
    with pd.ExcelWriter('youtube_channel_data.xlsx', engine='openpyxl') as writer:
        channel_df.to_excel(writer, sheet_name='Channel Info', index=False)
        videos_df.to_excel(writer, sheet_name='Videos', index=False)

if __name__ == "__main__":
    main()
```

### Data Processing

Once the data was collected, I processed it using Pandas and saved it to an Excel file. This file contains two sheets: one for channel information and one for video details.

### Data Visualization

With the data ready, I moved on to creating the dashboard in Power BI. The dashboard includes:

- **Lifetime Stats**: Total likes, comments, videos, and subscribers.
- **View Metrics**: Total views, monthly views, and weekly views.
- **Top 5 Best Performing Videos**: A bar chart showing the top videos based on likes.
- **Engagement Over Time**: A line chart showing view count by year and by month for the current year.

- ![image](https://github.com/RunnyEgg/Youtube-Dashboard/assets/145708300/638dd477-8e6b-4b43-a0b7-e2dbe80ec0e4)


## Key Learnings

Through this project, I gained a deeper understanding of:

- **API Integration**: Learned how to interact with the YouTube Data API v3 and handle large datasets.
- **Python Skills**: Enhanced my python knowledge and gained useful information on how to use APIs within it.
- **Data Processing**: Enhanced my skills in data manipulation using Pandas.
- **Data Visualization**: Improved my ability to create interactive and insightful dashboards using Power BI.
- **Project Management**: Developed a systematic approach to planning and executing data analysis projects.

## What I Would Like To Do In The Future

- **Advanced Analytics**: Implement predictive modeling for future view counts.
- **Interactivity**: Add more interactive elements to the dashboard, such as filters and drill-down capabilities.
- **Data Enrichment**: Explore other data sources and APIs to enrich the analysis further.

## Project Structure

```
├── youtube_scraper.py       # Python script for data scraping
├── youtube_channel_data.xlsx # Excel file with the scraped data
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── AliensRock Channel Performance Dashboard.pbix  # Power BI dashboard file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

