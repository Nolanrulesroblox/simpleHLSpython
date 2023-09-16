# simpleHLSpython
A Simple HLS demo in python3 (with ffmpeg)

# What it does
This Python script automates the process of creating HLS streams from a video file and an audio file. It offers two key features:

### Video Compression:
The script uses FFmpeg to compress the video using the H.264 codec. You can adjust the compression settings by modifying the Constant Rate Factor (CRF) and resolution values in the script.

### Audio Without Sound:
It generates an HLS stream for the audio with no sound. This is useful when you want to separate the audio and video streams, allowing you to control audio playback separately.

# How to Use:
To use this script, follow these steps:

### Prerequisites:
Ensure you have Python installed on your system. You'll also need FFmpeg installed, which is used for video and audio processing.

### Setup:
Place the script in a directory where your video file (video.mp4) and audio file (video.mp3 or video.mp4) are located. Update the video_file and audio_file variables with the correct filenames if necessary.

### Run the Script:
Open a terminal or command prompt, navigate to the directory containing the script, and execute it using the python script_name.py command.

### Output:
The script will create an output_hls directory where it stores the HLS streams and a master playlist (master.m3u8). You can host these HLS files on a web server for streaming.

What's Needed to Run It
To run this script, you need the following:
```
Python installed on your system (Python 3 recommended).
FFmpeg installed and accessible from the command line.
Input video and audio files (e.g., video.mp4 and video.mp3) in the same directory as the script.
An internet connection to fetch the audio file if you specify an external URL (modify the audio_url variable if needed).
Adequate storage space for the generated HLS files and playlists.
```
Once you've met these requirements, you can use the script to efficiently create HLS streams with video compression, separate audio without sound, and encryption for secure content delivery.
