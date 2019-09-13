from .downloader import YoutubeDownloader 
import subprocess
import os.path
import os

class AwesomeDownloader(YoutubeDownloader):

    def download(self, youtube_url, label, dest_path):
        if not os.path.exists(dest_path):
            raise FileNotFoundError("Cannot find the dest path")
        
        file_name = os.path.join(dest_path, label + ".%(ext)s")

        cmd_arguments = ['youtube-dl', '-f', 'bestaudio', '--audio-quality', '0', youtube_url, '-x', '--audio-format', 'mp3', '-o', file_name]
        print(' '.join(cmd_arguments))
        subprocess.call(cmd_arguments, shell=True)


if __name__ == "__main__":
    a = AwesomeDownloader()
    a.download("https://www.youtube.com/watch?v=JFYVcz7h3o0", "amonamon", "C:\\Users\\matan\\Music\\test")