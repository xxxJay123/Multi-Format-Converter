import os
from PIL import Image
from pillow_heif import register_heif_opener
import ffmpeg

# 註冊HEIF文件打開器
register_heif_opener()

source_dir = './Unconverted'
output_dir = './Converted'

# 如果輸出目錄不存在，則創建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍歷源目錄中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if filename.lower().endswith(('.heic')):
        # 處理HEIC文件
        with Image.open(file_path) as img:
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')
            img.save(output_path, 'JPEG')
            print(f"Converted {filename} to {os.path.basename(output_path)}")
    
    elif filename.lower().endswith(('.mov')):
        # 處理MOV文件
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.mp4')
        try:
            ffmpeg.input(file_path).output(output_path, vcodec='libx264', acodec='aac').run(overwrite_output=True)
            print(f"Converted {filename} to {os.path.basename(output_path)}")
        except ffmpeg.Error as e:
            print(f"Error converting {filename}: {e.stderr.decode() if e.stderr else 'Unknown error'}")

print("轉換完成！")