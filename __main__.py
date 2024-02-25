from tkinter import *
from random import *

root = Tk()
root.title('Auto_Name-v1.0.0')
WIDTH = str((root.winfo_screenwidth())//3)
HEIGHT = str((root.winfo_screenheight())//5)
root_size = '400x350+'+WIDTH+'+'+HEIGHT
root.geometry(root_size)

password=None

def Password():
    global password
    password=chr(randint(65,90))
    for i in range(5):
        password+=chr(randint(97,122))
    for i in range(6):
        password+=chr(randint(48,57))
    Password_Text = Label(root,text=password,font=('TkCaptionFont',14))
    Password_Text.place(anchor='center',relx='0.5',rely='0.35')

Title = Label(root,text='Auto_Name昵称生成器',font=('TkCaptionFont',18))
Title.pack()

From = Label(root,text='By Redsep3030',font=('TkCaptionFont',12))
From.place(anchor='center',relx='0.5',rely='0.93')

Text_Frame = Frame(width='350',height='40',highlightthickness='2',highlightbackground='black',highlightcolor='black')
Text_Frame.place(anchor='center',relx='0.5',rely='0.35')

Spawn_Button = Button(root,text='生成',bd='3',width='25',height='2',relief='ridge',command=Password)
Spawn_Button.place(anchor='center',relx='0.5',rely='0.5')

root.mainloop()