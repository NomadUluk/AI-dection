from tkinter import *
from PIL import ImageTk, Image
import webbrowser

vers = Tk()
vers.title("Информация об программе")
screen_width = vers.winfo_screenwidth()
screen_height = vers.winfo_screenheight()
window_width = 420
window_height = 260
w = int((screen_width - window_width) // 2)
l = int((screen_height - window_height) // 4)
vers.geometry(f"{window_width}x{window_height}+{w}+{l}")
vers.iconbitmap("v6_2.ico")

lb1= Label(vers,font=("Arial Bold",16),text="Информация о создании программы")
lb1.grid(row=0,column=1)
y = Image.open("info.png")
y.thumbnail((50,50))
y1 = ImageTk.PhotoImage(y)
foto = Label(vers, image=y1,borderwidth=0)
foto.grid(row=0,column=0,padx=5,pady=5)

lb2= Label(vers,font=("Arial Bold",16),text="Язык программирования: Python")
lb2.grid(row=1,column=1)
p = Image.open("python.jpg")
p.thumbnail((50,50))
p1 = ImageTk.PhotoImage(p)
foto2 = Label(vers, image=p1,borderwidth=0)
foto2.grid(row=1,column=0,padx=5,pady=5)

lb3 = Label(vers,font=("Arial Bold",16),text="Дата создания: 16.05.2023")
lb3.grid(row=3,column=1)
lb4 = Label(vers,font=("Arial Bold",16),text="Дата публикации: 22.05.2023")
lb4.grid(row=4,column=1)
lb5 = Label(vers,font=("Arial Bold",16),text="Версия: 1.0 ")
lb5.grid(row=5,column=1)
lb6 = Label(vers,font=("Arial Bold",16),text="Все права принадлежат автору!")
lb6.grid(row=6,column=1)

link_label = Label(vers,font=("Arial Bold",16), text="Github/NomadUluk", fg="blue", cursor="hand2")
link_label.grid(row=7,column=1)

link_label.bind("<Button-1>", lambda  event: open_link())
def open_link():
    webbrowser.open("https://github.com/NomadUluk")

vers.bind("<Escape>", lambda event: vers.quit())
vers.mainloop()