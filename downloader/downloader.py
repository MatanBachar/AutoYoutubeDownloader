import abc

class YoutubeDownloader(abc.ABC):
    '''Interface for youtube downloader'''

    @abc.abstractclassmethod
    def download(self, youtube_url, label, dest_path, override):
        """Given a url for a youtube video, downloads a mp3 file into speceific destination path

        :param youtube_url: URL address of the song
        :param label: The new file name
        :param dest_path: Destination directory for the file
        :param override: Whether overriding an existing songs 

        :return: (bool) True is the file has been downloaded successfuly, False otherwise.
        """
        pass
    @abc.abstractclassmethod
    def download_playlist(self, youtube_url, playlist_name, dest_path, override):
        """Given a url of a youtube playlist, this function download the whole playlists songs

        :param youtube_url: URL address of the playlist
        :param dest_path: Destination directory for the file
        :param playlist_name: Name of the playlist
        :param override: Whether overriding an existing songs 

        :return: (bool) True is the file has been downloaded successfuly, False otherwise.
        """
        pass