from .searcher import YoutubeSearcher 
import urllib.request
import urllib.parse
import re

SEARCH_URL = "http://www.youtube.com/results?"
PREFIX_WATCH = "http://www.youtube.com/watch?v="

class CoolSearcher(YoutubeSearcher):
    
    def search(self, query):
        query_string = urllib.parse.urlencode({"search_query" : query})
        html_content = urllib.request.urlopen(SEARCH_URL + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        
        for result in self.__filter_dups(search_results): # For some reasons sometimes you get duplicates of the same results
            yield PREFIX_WATCH + result


    def __filter_dups(self, elements):
        """Filter duplicate elements from list but keeps the order

        :param elements: List of elements
        :return: (list) List of elements without duplicates
        """
        seen = set()
        seen_add = seen.add
        return [x for x in elements if not (x in seen or seen_add(x))]

    

  