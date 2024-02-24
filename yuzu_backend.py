import yt_dlp

def main(url):
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(url)