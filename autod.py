import argparse
import os.path
import csv
from searcher.cool_searcher import CoolSearcher
from downloader.awesome_downloader import AwesomeDownloader
from fetcher.fabulous_fetcher import FabulousFetcher

def dir_exists(value):
    if not os.path.exists(value):
        raise argparse.ArgumentTypeError("Destination directory does not exists")
    return value

def get_args():
    parser = argparse.ArgumentParser(description='Short sample app')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--txt',          metavar='FILENAME',           type=argparse.FileType('r', encoding='utf-8-sig'),
                             help='Download multiple songs with a given list from file. Song names seperated by newlines')
    group.add_argument('-c', '--csv',          metavar='FILENAME',           type=argparse.FileType('r', encoding='utf-8-sig'),
                             help="""Download multiple songs with a given list from csv file.
                                     Each line represent a song, each song represented by song name and artist name
                                     seperated by comma.""")
    group.add_argument('-s', '--single',        metavar='NAME',               type=str,
                             help='Download speceific song by name')
    group.add_argument('-p', '--playlist',      metavar='URL playlist_name',  type=str,   nargs=2,
                             help='Download a whole playlist from youtube')
    group.add_argument('--fetch-only',         action='store_true',    default=False,   dest="fetch",
                             help='Fetches songs metadata from spotify')
    parser.add_argument('-o',                   action='store_true',    default=False,   dest="override",
                             help='Override existing songs')
    parser.add_argument('dest',                 metavar='DEST_DIR',     type=dir_exists,
                             help='Destination directory for your new songs')
    return parser.parse_args()


def fetch_dir(s_fetcher, directory='.'):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(directory):
            for file in f:
                if '.mp3' in file:
                    files.append(os.path.join(r, file))
    for f in files:
        s_fetcher.fetch_metadata(f)


def main():
    args = get_args()

    # Creating my awesome and cool helpers    
    youtube_searcher = CoolSearcher()
    youtube_downloader = AwesomeDownloader()
    songs_fetcher = FabulousFetcher()

    if args.txt:
        # Iterates over the song in the txt and searches for them in youtube
        for song in args.txt.readlines():
            print(song.strip())
            # Takes the first result from youtube, appending hq (high quality) to the key word for better result
            result = next(youtube_searcher.search(song + " hq" if song.isalpha() else song))
            youtube_downloader.download(result, song.strip(), args.dest, args.override)
            songs_fetcher.fetch_metadata(os.path.join(args.dest, f'{song.strip()}.mp3'))

    if args.fetch:
        fetch_dir(songs_fetcher ,args.dest)

    if args.csv:
        reader = csv.reader(args.csv, delimiter=',')
        print("CSV file detected.")
        for song, artist in reader:
            print(f"{song.strip()} by {artist.strip()}")
            query = f'{artist} {song}'
            result = next(youtube_searcher.search(query + " hq" if song.isalpha() else query))
            youtube_downloader.download(result, query, args.dest, args.override)
            
            songs_fetcher.fetch_metadata(os.path.join(args.dest, f'{query}.mp3'))

    if args.single:
        # Search for specific song in youtube
        result = next(youtube_searcher.search(args.single.strip() + " hq" if args.single.isalpha() else args.single))
        youtube_downloader.download(result, args.single.strip(), args.dest, args.override)

    if args.playlist:
        # URL is already given so no need to for searching
        youtube_downloader.download_playlist(args.playlist[0], args.playlist[1], args.dest, args.override)
        fetch_dir(args.dest)

if __name__ == "__main__":
    main()