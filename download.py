from pytube.cli import on_progress
import pytube
import os

def vid_download(url, path):
    # path = os.path.join(os.path.expanduser('~'), "Downloads", "Youtube")
    yt = pytube.YouTube(url, on_progress_callback=on_progress)

    stream = yt.streams.filter(type="video", file_extension="mp4")
    # stream = yt.streams.filter(type="audio").get_audio_only()


    print("Downloading(" + "{:.2f}".format(stream.filesize / 1024 / 1024) + " MB): ")
    stream.download(output_path=path)

    print()

def out(str):
    print(str)