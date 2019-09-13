import argparse
import os.path
from searcher.cool_searcher import CoolSearcher

def dir_exists(value):
    if not os.path.exists(value):
        raise argparse.ArgumentTypeError("Destination directory does not exists")
    return value

def get_args():
    parser = argparse.ArgumentParser(description='Short sample app')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', metavar='FILENAME', type=argparse.FileType('r', encoding='utf8'),
                             help='Download multiple songs with a given list from file. Song names seperated by newlines')
    group.add_argument('-s', '--single', metavar='URL', type=str,
                             help='Download speceific song by URL')
    group.add_argument('-p', '--playlist', metavar='URL', type=str,
                             help='Download a whole playlist from youtube')
    parser.add_argument('dest'           , metavar='DEST_DIR', type=dir_exists,
                             help='Destination directory for your new songs')

    return parser.parse_args()


def main():
    args = get_args()
    print(type(args.file), dir(args.file))
    if args.file:
        for song in args.file.readlines():
            print(song, end='')
    youtube_searcher = CoolSearcher()
    for result in youtube_searcher.search("amon amarth twilight of the thunder god hq"):
        print(result)
    

if __name__ == "__main__":
    main()