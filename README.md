## YouTube Video Downloader

This Python script allows you to download YouTube videos and save them as MP4 files. It utilizes the `pytube` and `moviepy` libraries to handle the downloading and processing of videos.

### Prerequisites

Make sure you have the following libraries installed before running the script:

- `pytube`
- `moviepy`
- `datetime`

You can install these libraries using pip:

```
pip install pytube moviepy
```

### Usage

1. Run the script using Python.
2. When prompted, enter the YouTube video link you want to download. For example: `https://www.youtube.com/watch?v=f6YDKF0LVWw`.
3. The script will attempt to download the video from the provided link.
4. If the video is available, the script will display information about the video, such as its title, length, views, ratings, and description.
5. The script will then download the video in 1080p resolution and save it as an MP4 file.
6. It will also extract the audio from the video and save it as an MP3 file.
7. Finally, the script will combine the video and audio into a single MP4 file, using the video's title as the filename.
8. The temporary video and audio files will be deleted after the combination process is complete.
9. The script will print a success message once the download and processing are finished.

Please note that the availability of video streams and their quality may vary depending on the YouTube video.

### Example

```python
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
user_input = str(input("Enter the YouTube video link: "))
yt_download(user_input)
```

Note: The above example is interactive, where the user is prompted to enter the YouTube video link. You can modify the script to accept the link in a different way if desired.