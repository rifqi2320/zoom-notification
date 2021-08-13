from tkinter.constants import LEFT
from PIL import ImageChops
from PIL import Image
import tkinter as tk

from screenshotWindow import get_chat_ss
import winsound


window = tk.Tk()
window.title("App nya iqi")


paused = False

old_im = Image.open("test.png")

def tick():
    global paused, tkimg, old_im, im
    # Do something
    im = get_chat_ss()
    im.save("test.png")
    diff = ImageChops.difference(im, old_im)
    if diff.getbbox():
        winsound.Beep(2500,300)
        old_im = im


    if not paused:
        window.after(500, tick)


def Start():
    global paused
    paused = False
    tick()
    window.configure(bg='green')

def Stop():
    global paused
    paused = True
    window.configure(bg='grey')

startbtn = tk.Button(window, text="Start", command=Start)
startbtn.pack(side=LEFT)

stopbtn = tk.Button(window, text="Stop", command=Stop)
stopbtn.pack(side=LEFT)



window.mainloop()