import time
import yt_dlp

def VK_download_video(url: str, filename):
    name = str(time.time())
    try:
        ydl_opts = {'outtmpl': f'VK_files/{filename}'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 1 # Успешно скачано
    except:
        return 0 # Неверная ссылка
