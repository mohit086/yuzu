import tempfile
import os

def extract_file(params):
    temp_dir = tempfile.mkdtemp()
    url = params['url']
    command = f'yt-dlp {url} -o {temp_dir}/%(title)s.%(ext)s'
    os.system(command)
    extracted_file = os.path.join(temp_dir, os.listdir(temp_dir)[0])
    filename = os.path.basename(extracted_file)
    return extracted_file, filename