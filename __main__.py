from tkinter import *
from os import *

root = Tk()
root.title('Auto_Name-1.0')
WIDTH = str((root.winfo_screenwidth())//3)
HEIGHT = str((root.winfo_screenheight())//5)
root_size = '400x350+'+WIDTH+'+'+HEIGHT
root.geometry(root_size)

text = Label(root,text='Auto_Name昵称生成器',font=('TkCaptionFont',18))

text.pack()

root.mainloop()