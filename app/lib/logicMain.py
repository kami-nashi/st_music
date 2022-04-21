from __future__ import unicode_literals

import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('[youtube-dl] Done downloading, now converting ...')

def musicDownload(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/tmp/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)

        iMaxDuration = int(600)
        iDuration = info_dict["duration"]
        if iDuration > iMaxDuration:
            print(
                "[youtube-dl] Too long to download, %ds > %ds" %
                (iDuration, iMaxDuration))
            print("[youtube-dl]", info_dict["id"], "processing complete ...")
        else:
            print("[youtube-dl] Downloading","'" + info_dict["title"] + "'...", "as", info_dict["id"] + '.mp3', 'from', url)
            ydl.download([url])
            print("[youtube-dl]", info_dict["id"], "processing complete ...")

    return ydl_opts
