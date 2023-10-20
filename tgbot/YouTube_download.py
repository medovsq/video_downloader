from pytube import YouTube
from config import YOUTUBE_PATH


def download_video(url: str, filename: str, path=YOUTUBE_PATH):
    try:
        stream = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    except:
        return 0  # если ссылка недействительна
    if stream.filesize_mb > 512:
        return -1  # если файл слишком большой
    stream.download(
        filename=filename,
        output_path=path,
    )
    return 1  # если файл успешно скачан

