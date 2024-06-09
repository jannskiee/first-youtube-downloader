
# YouTube Video Downloader

This script downloads a YouTube video and its audio, merges them, and saves the result as an MP4 file.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pytube` library
- `moviepy` library

You can install the required libraries using pip:

```sh
pip install pytube3 moviepy
```

## Usage

1. **Run the script**:
   ```sh
   python main.py
   ```

2. **Input the YouTube video link**:
   When prompted, enter the URL of the YouTube video you want to download.

## How It Works

1. **Download the video and audio**:
   The script downloads the video in 1080p resolution and the audio stream separately.

2. **Merge video and audio**:
   Using `moviepy`, it merges the video and audio streams into a single MP4 file.

3. **Save and clean up**:
   The merged video is saved with the YouTube video's title as the filename. Temporary files are removed after merging.

## Example

Run the script and enter a YouTube link, such as:

```
https://www.youtube.com/watch?v=f6YDKF0LVWw
```

The script will download and merge the video and audio, then save it as `POP! by Nayeon.mp4`.

## Error Handling

- If the video is unavailable, the script will print an error message.
- The script provides information about the video such as title, length, views, rating, and description before downloading.

## Code Explanation

Here is a brief overview of the code:

```python
import os
import datetime
import moviepy.editor as mpe
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def yt_download(link):
    try:
        yt = YouTube(link)
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
```

## Acknowledgments

- This script uses the `pytube` library for downloading YouTube videos.
- The `moviepy` library is used for video and audio processing.

---

Feel free to modify the README as needed to better fit your specific use case or preferences.