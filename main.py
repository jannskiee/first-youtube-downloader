import os
import datetime
import moviepy.editor as mpe
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def yt_download(link):
    try:
        yt = YouTube(user_input)
    except VideoUnavailable:
        print("Video is unavailable")
    else:
        print(f"\nDownloading {user_input} ({yt.title})...")
        print("-------------------------------------------------------------------------------------------------------")
        print(f"Title: {yt.title}")
        print(f"Length: {(str(datetime.timedelta(seconds=yt.length)))}")
        print(f"Views: {yt.views} views")
        print(f"Ratings: {yt.rating}")
        print(f"Description: {yt.description}")
        print("-------------------------------------------------------------------------------------------------------")

        video = yt.streams.filter(res="1080p").first().download()
        os.rename(video, f"video.mp4")

        audio_stream = yt.streams.filter(only_audio=True)
        audio = audio_stream[0].download()
        os.rename(audio, f"audio.mp3")

        video_clip = mpe.VideoFileClip("video.mp4")
        audio_clip = mpe.AudioFileClip("audio.mp3")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(f"{yt.title}.mp4")

        os.remove("video.mp4")
        os.remove("audio.mp3")
        print(f"\nDownloaded {user_input} ({yt.title}) successfully!")


# Example Link: https://www.youtube.com/watch?v=f6YDKF0LVWw (POP! by Nayeon)
user_input = str(input("Enter the youtube video link: "))
yt_download(user_input)
