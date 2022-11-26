# --- coding: utf-8 ---
# @FileName  :youtube_video_downloader.py
# @Time      :11/26/2022 5:59 PM
# @Author    :Abraham
# @Software  :PyCharm

from pytube import YouTube


def Download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("An error occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL link: ")
Download(link=link)
