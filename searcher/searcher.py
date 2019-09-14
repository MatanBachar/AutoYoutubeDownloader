import abc

class YoutubeSearcher(abc.ABC):
    '''Interface for youtube searcher'''

    @abc.abstractclassmethod
    def search(self, query):
        """Serach for video results in youtube

        :param query: String of the video's name to search
        :yield: Next result 
        """
        pass