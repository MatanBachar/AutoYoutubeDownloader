from .downloader import YoutubeDownloader 
import shutil
import subprocess
import os.path
import os


class AwesomeDownloader(YoutubeDownloader):

    def download(self, youtube_url, label, dest_path, override):
        if not os.path.exists(dest_path):
            raise FileNotFoundError("Cannot find the dest path")
        
        # In case the label is not with latin letters the label change temporarilly
        file_name = os.path.join(dest_path,"temp_label" + ".%(ext)s")
        cmd_arguments = ['youtube-dl', '-f', 'bestaudio', '--audio-quality', '0', youtube_url, '-x', '--audio-format', 'mp3', '-o', file_name]

        file_name = file_name.replace("%(ext)s", "mp3")
        new_name = file_name.replace("temp_label", label)

        # In case the song is already exists
        if os.path.exists(new_name):
            if not override:
                print("Song already exists here. Skipping...")
                return False
            print("OVERRIDE ACTIVATED: Overriding existing song...")
            os.remove(new_name)
        subprocess.call(cmd_arguments, shell=True)
        try:
            os.rename(file_name, new_name)
        except:
            print("Failed Downloading file")
        return True

    def download_playlist(self, youtube_url, playlist_name, dest_path, override):
        if not os.path.exists(dest_path):
            raise FileNotFoundError("Cannot find the dest path")
        playlist_dir = os.path.join(dest_path, playlist_name)
        if os.path.exists(playlist_dir):
            if not override:
                print("Playlist already exists here. Skipping...")
                return False
            print("OVERRIDE ACTIVATED: Overriding existing playlist...")
            shutil.rmtree(playlist_dir)
    
        os.mkdir(playlist_dir)
        file_name = "%(title)s.%(ext)s"
        cmd_arguments = ['youtube-dl', '-f', 'bestaudio', '--audio-quality', '0', youtube_url, '-x', '--audio-format', 'mp3', '-o', os.path.join(playlist_dir, file_name)]
        subprocess.call(cmd_arguments, shell=True)
        return True

if __name__ == "__main__":
    a = AwesomeDownloader()
    a.download("https://www.youtube.com/watch?v=JFYVcz7h3o0", "amonamon", "C:\\Users\\matan\\Music\\test")