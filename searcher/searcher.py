import abc

class YoutubeSearcher(abc.ABC):
    '''Interface for youtube searcher'''
    @abc.abstractclassmethod`
    def search(self, query):
        '''Serach for video results in youtube'''
        pass