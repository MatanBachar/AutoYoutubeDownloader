from searcher.cool_searcher import CoolSearcher


def main():
    youtube_searcher = CoolSearcher()
    for result in youtube_searcher.search("amon amarth twilight of the thunder god hq"):
        print(result)
    

if __name__ == "__main__":
    main()