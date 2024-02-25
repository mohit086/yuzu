import yt_dlp

def download_file(params):

    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(params['url'])