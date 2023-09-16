import subprocess
import os
# Input video file and audio file
video_file = "video.mp4"
audio_file = "video.mp4"
# Check if the file exists
if !os.path.exists(audio_file):
    audio_file = "video.mp3"
# Output directory for HLS streams and playlist
output_directory = "output_hls/"
# Set the segment duration (in seconds) This splits the stream into chunks per x
segment_duration = 10
# Set the Constant Rate Factor (CRF) for video compression
# Adjust the CRF value as needed (lower values for higher quality)
crf_value = "23"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)
# FFmpeg command to generate video segments with no audio and compression
video_command = [
    "ffmpeg",
    "-i", video_file,
    "-c:v", "libx264",
    "-crf", crf_value,  # Adjust CRF value for quality/compression trade-off
    "-an",  # Disable audio stream
    "-hls_time", str(segment_duration),
    "-hls_list_size", "0",  # Generates an extended M3U playlist
    "-hls_segment_filename", f"{output_directory}video%03d.ts",
    f"{output_directory}video_playlist.m3u8"
]

# Run FFmpeg
subprocess.run(video_command)

# FFmpeg command to generate audio segments with no audio
audio_command = [
    "ffmpeg",
    "-i", audio_file,
    "-vn",  # Disable audio stream
    "-c:a", "aac",
    "-hls_time", str(segment_duration),
    "-hls_list_size", "0",  # Generates an extended M3U playlist
    "-hls_segment_filename", f"{output_directory}audio%03d.ts",
    f"{output_directory}audio_playlist.m3u8"
]

# Run FFmpeg
subprocess.run(audio_command)

# Create the HLS playlist (index.m3u8) with relative URLs for audio
with open(f"{output_directory}video_playlist.m3u8", "r") as video_playlist_file:
    video_playlist = video_playlist_file.readlines()

with open(f"{output_directory}audio_playlist.m3u8", "r") as audio_playlist_file:
    audio_playlist = audio_playlist_file.readlines()

# Create the index.m3u8 file with the necessary information
with open(f"{output_directory}index.m3u8", "w") as index_file:
    index_file.write("#EXTM3U\n")
    index_file.write("#EXT-X-VERSION:3\n")
    index_file.write("#EXT-X-STREAM-INF:BANDWIDTH=2000000\n")
    index_file.write("video_playlist.m3u8\n")
    index_file.write("#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID=\"audio\",NAME=\"English\",DEFAULT=YES,AUTOSELECT=YES,URI=\"audio_playlist.m3u8\"\n")
    index_file.write(f"{output_directory}audio_playlist.m3u8\n")

print(f"HLS streams generated with video compression (CRF {crf_value}) and audio.ts with no audio.")
