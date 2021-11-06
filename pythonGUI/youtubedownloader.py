import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from PIL import *
import PIL as pl
def widgets():
    CharPhoto = PhotoImage(file="youtube.gif")
    ChLabel = Label(root, image=CharPhoto,bd=7)
    ChLabel.place(x=40,y=40)
    head1 = Label(root,width=30,text="YOUTUBE DOWNLOADER ",font=("arial",20),bg="aqua",fg="black")
    head1.place(x=170,y=60)
    head2 = Label(root,width=20,text="Paste Your Link Here:->",font=("arial",12),bg="aqua",fg="black")
    head2.place(x=100,y=120)
    entry1 = Entry(root,width=40,relief=GROOVE,bd=7,textvariable=video_Link)
    entry1.place(x=290,y=120)
    head3 = Label(root,width=20,text="Path To Save Videos:->",font=("arial",12),bg="aqua",fg="black")
    head3.place(x=100,y=170)
    entry2 = Entry(root,width=40,relief=GROOVE,bd=7,textvariable=download_Path)
    entry2.place(x=290,y=170)
    button1 = Button(root,text="Browse Path",height=6,bg="aqua",fg="black",font=("arial",12),bd=6,command=browse)
    button1.place(x=650,y=120)
    button2 = Button(root,text="Download Here",bg="aqua",fg="black",font=("arial",20),bd=6,command=download)
    button2.place(x=290,y=260)
def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH",title="Save Videos")
    download_Path.set(download_directory)
def download():
    video_link = video_Link.get()
    download_Folder = download_Path.get()
    get_video = YouTube(video_link)
    Video_stream = get_video.streams.first()
    Video_stream.download(download_Folder)
    messagebox.showinfo("Video is downloaded successfully and saved in " + download_Folder)
root = Tk()
root.title("YOUTUBEDOWNLOADER")
root.geometry("800x600")
root.config(bg="red")
video_Link = StringVar()
download_Path = StringVar()
root.resizable(0,0)
widgets()
root.mainloop()