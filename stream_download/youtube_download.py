from pytube import YouTube

url = 'https://www.youtube.com/watch?v=bZHYQnAR5fw'
YouTube(url).streams.first().download()
# yt = YouTube(url)
# yt.streams.filter(progressive=True, file_extension='mp4').order_by(
#    'resolution').desc().first().download()
