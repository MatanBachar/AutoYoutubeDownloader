import argparse
import os.path
import csv
from searcher.cool_searcher import CoolSearcher
from downloader.awesome_downloader import AwesomeDownloader

def dir_exists(value):
    if not os.path.exists(value):
        raise argparse.ArgumentTypeError("Destination directory does not exists")
    return value

def get_args():
    parser = argparse.ArgumentParser(description='Short sample app')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file',          metavar='FILENAME',           type=argparse.FileType('r', encoding='utf8'),
                             help='Download multiple songs with a given list from file. Song names seperated by newlines')
    group.add_argument('-c', '--csv',          metavar='FILENAME',           type=argparse.FileType('r', encoding='utf8'),
                             help="""Download multiple songs with a given list from csv file.
                                     Each line represent a song, each song represented by song name and artist name
                                     seperated by comma.""")
    group.add_argument('-s', '--single',        metavar='NAME',               type=str,
                             help='Download speceific song by name')
    group.add_argument('-p', '--playlist',      metavar='URL playlist_name',  type=str,   nargs=2,
                             help='Download a whole playlist from youtube')
    parser.add_argument('-o',                   action='store_true',    default=False,   dest="override",
                             help='Override existing songs')
    parser.add_argument('dest',                 metavar='DEST_DIR',     type=dir_exists,
                             help='Destination directory for your new songs')
    return parser.parse_args()


def main():
    args = get_args()

    # Creating my awesome and cool helpers    
    youtube_searcher = CoolSearcher()
    youtube_downloader = AwesomeDownloader()

    if args.file:
        # Iterates over the song in the file and searches for them in youtube
        for song in args.file.readlines():
            print(song.strip())
            # Takes the first result from youtube, appending hq (high quality) to the key word for better result
            result = next(youtube_searcher.search(song + " hq" if song.isalpha() else song))
            youtube_downloader.download(result, song.strip(), args.dest, args.override)
    if args.csv:
        reader = csv.reader(args.csv, delimiter=',')
        print("CSV file detected.")
        for song, artist in reader:
            print("{song_name} by {artist}".format(song_name=song.strip(), artist=artist.strip()))
            query = artist + ' ' + song
            result = next(youtube_searcher.search(query + " hq" if song.isalpha() else query))
            file_name = artist + ' - ' + song
            youtube_downloader.download(result, file_name, args.dest, args.override)

    if args.single:
        # Search for specific song in youtube
        result = next(youtube_searcher.search(args.single.strip() + " hq" if args.single.isalpha() else args.single))
        youtube_downloader.download(result, args.single.strip(), args.dest, args.override)
    if args.playlist:
        # URL is already given so no need to for searching
        youtube_downloader.download_playlist(args.playlist[0], args.playlist[1], args.dest, args.override)

if __name__ == "__main__":
    main()