import Tkinter as tk
import subprocess as sp
import os

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))
    extProc = sp.Popen(['git','pull'])
    (message, err) = extProc.communicate()
    print message
    extProc = sp.Popen(['python','run.py'])
    root.quit()
    root.destroy()


root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
text.insert('end', "Hello from github!")
root.mainloop()
