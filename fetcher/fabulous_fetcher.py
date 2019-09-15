# from .fetcher import SongFetcher
import addMetadata as beutifymp3
import requests

CONFIG = None
GENIUS_KEY = None
SP_SECRET = None
SP_ID = None
config_path = None

MAX_TRIES = 10

class FabulousFetcher(object):
    def __init__(self):
        beutifymp3.setup_config()
    
    def fetch_metadata(self, filename):
        print(filename)
        is_needed_fix = None
        for _ in range(MAX_TRIES):
            if is_needed_fix is None:
                try:
                    is_needed_fix = beutifymp3.fix_music_file(beutifymp3.get_spotify_adapter(), filename, False, '{title}')
                except requests.exceptions.ConnectionError as e:
                    print("Connection error to Spotify, trying again", e)
                except AttributeError:
                    print("Can't fetch metadata for this file, skipping...")
                    break
            else:
                break
        return is_needed_fix
        


if __name__ == "__main__":
    f = FabulousFetcher()
    f.fetch_metadata("Slow Ride - Foghat.mp3")