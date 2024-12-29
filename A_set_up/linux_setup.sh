#!/bin/bash

# 安装Python库
pip install Pillow pillow-heif ffmpeg-python

# 检查FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg could not be found."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y ffmpeg
    elif command -v yum &> /dev/null; then
        sudo yum install -y ffmpeg
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y ffmpeg
    elif command -v brew &> /dev/null; then
        brew install ffmpeg
    else
        echo "无法自动安装FFmpeg，请手动安装。"
    fi
else
    echo "FFmpeg is already installed."
fi

echo "Setup complete. Please restart your terminal for changes to take effect."