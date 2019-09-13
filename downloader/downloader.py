import abc

class YoutubeDownloader(abc.ABC):
    '''Interface for youtube downloader'''

    @abc.abstractclassmethod
    def download(self, youtube_url, label, dest_path):
        '''Given a url for a youtube video, downloads a mp3 file into speceific destination path'''
        pass