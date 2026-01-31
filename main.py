from moviepy.editor import ColorClip

print("🎬 بدء تشغيل المصنع...")

# فيديو مدته 5 ثواني (خلفية زرقاء)
clip = ColorClip(size=(1080, 1920), color=(0, 0, 100), duration=5)

# حفظ الفيديو
clip.write_videofile("video.mp4", fps=24)

print("✅ تم بنجاح! الفيديو جاهز.")
