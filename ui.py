import tkinter as tk
from pytube.cli import on_progress
import pytube
import os
import download

def change_to_aud():
    audio_frame.pack(fill="both", expand=1,)
    main_frame.forget()
    video_frame.forget()

def change_to_vid():
    video_frame.pack(fill="both", expand=1,)
    main_frame.forget()
    audio_frame.forget()

# def vid_download():
    




if __name__ == "__main__":
    win = tk.Tk()
    win.title('YT Dowloader - by Patty')
    win.resizable(False,False)
    win.geometry('600x320+500+300')    

    main_frame = tk.Frame(win, bg="#BFB8AD")
    video_frame = tk.Frame(win, bg="#BFB8AD")
    audio_frame = tk.Frame(win, bg="#BFB8AD")
    
    main_frame.pack(fill="both", expand=1)

class mainPage():
    main_label1 = tk.Label(main_frame, text='Video or Audio ?', bg='#BFB8AD', font='zapfino 20')
    main_label1.place(anchor=tk.CENTER, x=300, y=60)

    main_vidbtn = tk.Button(main_frame, text='Video', width=15,command=change_to_vid)
    main_vidbtn.place(anchor=tk.CENTER, x=200, y=170)

    main_audbtn = tk.Button(main_frame, text='Audio', width=15,  command=change_to_aud)
    main_audbtn.place(anchor=tk.CENTER, x=400, y=170)

class vidPage():
    vid_label1 = tk.Label(video_frame, text='Enter Video Url',font='zapfino 20',bg='#BFB8AD')
    vid_label1.place(anchor=tk.CENTER, x=300, y=60)

    vid_enUrl = tk.Entry(video_frame, width=60, bd='3px')
    vid_enUrl.place(anchor=tk.CENTER, x=300, y=100)
    vid_enUrl.insert(0, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    vid_label2 = tk.Label(video_frame, text='Download Path', bg='#BFB8AD', font='zapfino 20')
    vid_label2.place(anchor=tk.CENTER, x=300, y=160 )

    vid_enPath = tk.Entry(video_frame, width=40, border='3px')
    vid_enPath.place(anchor=tk.CENTER, x=230, y=200)
    vid_enPath.insert(0, os.path.join(os.path.expanduser('~'), "Downloads", "YT"))

    vid_btn1 = tk.Button(video_frame, text='Download ~', command = lambda url=vid_enUrl.get(), path=vid_enPath.get(): download.vid_download(url, path) )
    vid_btn1.place(anchor=tk.CENTER, x=450, y=200)

class audPage():
    pass

win.mainloop()