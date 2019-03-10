import os
from tkinter import *
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog

root = Tk()


menubar = Menu(root)
root.config(menu=menubar)

# creating submenu
subMenu = Menu(menubar, tearoff = 0)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open", command = browse_file)
subMenu.add_command(label="Exit", command = root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About','This is a DJ build using tkinter.')
subMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About us", command = about_us)


mixer.init()

root.title("Chiki Chiki")
root.iconbitmap(r'mp3player.ico')

text = Label(root,text = 'AAG LAGATE HAIN!')
text.pack(pady=10)


def play_music():
    try:
        paused
    except NameError:
        try:
            mixer.music.load('faded.mp3')
            mixer.music.play()
            statusbar['text'] = "Playing Music" + '-' + os.path.basename('faded.mp3')
        except:
            tkinter.messagebox.showinfo('file not found','Chiki is upset . Please check again.')
    else:
        mixer.music.unpause()
        statusbar['text'] = "Resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Stopped"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Paused"

def rewind_music():
    play_music()
    statusbar['text'] = "Rewinded"




def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

muted = FALSE


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        volumeBtn.configure(image=volumephoto)
        scale.set(50)
        muted = FALSE



    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutephoto)
        scale.set(0)
        muted = TRUE


middleframe = Frame(root)
middleframe.pack(pady=30,padx=30)


playphoto = PhotoImage(file='playb.png')
playBtn = Button(middleframe, image=playphoto, command=play_music)
playBtn.grid(row=0,column=0,padx=10)


stopphoto = PhotoImage(file='stop.png')
stopBtn = Button(middleframe, image=stopphoto, command=stop_music)
stopBtn.grid(row=0,column=1,padx=10)

pausephoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleframe, image=pausephoto, command=pause_music)
pauseBtn.grid(row=0,column=2,padx=10)

bottomframe = Frame(root)
bottomframe.pack()

rewindphoto = PhotoImage(file='rewind.png')
rewindBtn = Button(bottomframe, image=rewindphoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

mutephoto = PhotoImage(file='mute.png')
volumephoto = PhotoImage(file='volume.png')
volumeBtn = Button(bottomframe, image=volumephoto, command=mute_music)
volumeBtn.grid(row=0,column=1)




scale = Scale(bottomframe,from_=0,to=100, orient=HORIZONTAL, command = set_vol)
scale.set(50)
mixer.music.set_volume(50)
scale.grid(row=0,column=2,pady=15,padx=30)

statusbar = Label(root,text="Welcome to RANGEELA DJ",relief = SUNKEN, anchor = W)
statusbar.pack(side=BOTTOM, fill = X)

root.mainloop()