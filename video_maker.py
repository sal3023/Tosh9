import os
import requests
from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout

# إعدادات الجودة
VIDEO_SIZE = (1920, 1080)
OUTPUT_FILE = "output_video.mp4"

def download_assets():
    print("Downloading Images...")
    images = []
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    # تحميل 5 صور عالية الجودة
    for i in range(5):
        url = f"https://picsum.photos/1920/1080?random={i}"
        response = requests.get(url)
        filename = f"assets/image_{i}.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)
        images.append(filename)
    return images

def create_video():
    image_files = download_assets()
    clips = []
    
    for img in image_files:
        # مدة كل صورة 3 ثواني
        clip = ImageClip(img).set_duration(3)
        clip = fadein(clip, 0.5)
        clips.append(clip)
        
    final_video = concatenate_videoclips(clips, method="compose")
    
    final_video.write_videofile(
        OUTPUT_FILE, 
        fps=24, 
        codec="libx264", 
        audio=False
    )
    print("Video Created Successfully!")

if __name__ == "__main__":
    create_video()
