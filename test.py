import subprocess

try:
    subprocess.run(['ffmpeg', '-version'], check=True, capture_output=True, text=True)
    print("FFmpeg is installed and accessible.")
except subprocess.CalledProcessError as e:
    print(f"FFmpeg is not accessible. Error: {e}")