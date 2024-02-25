import tempfile
import yt_dlp
import os

def extract_file(params):
    temp_dir = tempfile.mkdtemp()
    output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')
    params['outtmpl'] = output_template

    with yt_dlp.YoutubeDL(params) as ydl:
        ydl.download(params['url'])

    filename = os.path.basename(ydl.prepare_filename(ydl.extract_info(params['url'], download=True)))
    return os.path.join(temp_dir, filename), filename