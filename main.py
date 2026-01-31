from moviepy.editor import ColorClip
import random

print("🚀 جاري تشغيل المصنع لإنتاج 20 فيديو...")

# تكرار العملية 20 مرة
for i in range(1, 21):
    # لون عشوائي لكل فيديو
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # اسم الملف يتغير (video_1, video_2...)
    filename = f"video_{i}.mp4"
    
    # إنشاء الفيديو (مدة 2 ثانية ليكون سريعاً)
    clip = ColorClip(size=(1080, 1920), color=color, duration=2)
    clip.write_videofile(filename, fps=24)
    print(f"✅ تم صنع: {filename}")

print("🎉 انتهى! جميع الفيديوهات جاهزة.")
