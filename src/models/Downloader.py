import youtube_dl

from .Logger import Logger

class Downloader(object):

    options = None
    status = None
    on_download_complete_action = None

    def __init__(self):

        self.options = {
            'format': 'bestaudio/best',
            'outtmpl': './temp/%(title)s-%(id)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    title = None
    uploader = None

    def set_on_download_complete_action(self, function):
        self.on_download_complete_action = function

    def set_listener(self, listener):
        self.options['logger'] = Logger(listener)

    def download(self, url):
        with youtube_dl.YoutubeDL(self.options) as ydl:
            info_dict = ydl.extract_info(url, download = True)
            self.title = info_dict['title']
            self.uploader = info_dict['uploader']

        self.on_download_complete_action()
