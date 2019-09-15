import abc

class SongFetcher(abc.ABC):
    '''Interface for song fetcher'''

    @abc.abstractclassmethod
    def fetch_metadata(self, filename):
        """Fetches for metadata for the song.

        :param filename: Path to the file to fetch the data for
        :return: (bool) True is the metadata has been fetched into the file successfuly, False otherwise.
        """
        pass