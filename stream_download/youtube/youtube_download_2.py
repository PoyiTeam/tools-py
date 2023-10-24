from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc',
        'https://www.youtube.com/watch?v=403tAdvkSTA']
with YoutubeDL() as ydl:
    ydl.download(URLS)
