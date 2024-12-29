@echo off
setlocal enabledelayedexpansion

:: 安装Python库
python -m pip install Pillow pillow-heif ffmpeg-python

:: 检查FFmpeg路径
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg could not be found.
    echo Please ensure FFmpeg is installed and added to your PATH manually.
    echo You can download FFmpeg from: https://ffmpeg.org/download.html
) else (
    echo FFmpeg is already installed.
)

echo Setup complete. Please restart your command prompt for changes to take effect.