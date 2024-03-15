from pytube import YouTube
from pytube import Playlist
import os

def generate_path(playlist=False, play_name=''):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_name = "songs"
    folder_path = os.path.join(current_dir, folder_name)
    if playlist:
        folder_path = os.path.join(folder_path, play_name)
    return folder_path

def status_bar(done=1, total=1):
    print('[', end='')
    ratio = int(50 * done / total)
    for i in range (ratio):
        print('#', end='')
    for i in range (ratio, 50):
        print('.', end='')
    print('] Baixando:', str(done) + '/' + str(total), end='\r')

def final_message(name, playlist=False):
    n = max(1, 32 - int(len(name)/2))
    for i in range (n):
        print('=', end='')
    if playlist:
        print(" Playlist", name, "baixada!", end=' ')
    else:
        print(" Música", name, "baixada!", end=' ')
    for i in range (n):
        print('=', end='')

def mp4_download(yt, path):
    stream = yt.streams.get_audio_only()
    stream.download(path)

def main():
    url = input("Insira um link para um vídeo ou playlist: ")

    print("")

    if 'playlist' in url:
        p = Playlist(url)
        path = generate_path(True, p.title)
        i = 0
        for video in p.videos:
            i+=1
            status_bar(i, p.length)
            mp4_download(video, path)
        final_message(p.title, True)
    else:
        path = generate_path()
        yt = YouTube(url)
        status_bar()
        mp4_download(yt, path)
        final_message(yt.title)

    print("\n")


if __name__ == '__main__':
    main()