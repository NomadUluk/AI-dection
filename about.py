from tkinter import *
from PIL import ImageTk, Image
import webbrowser

myroot = Tk()
myroot.title("Информация об авторе")
screen_width = myroot.winfo_screenwidth()
screen_height = myroot.winfo_screenheight()
window_width = 420
window_height = 560
w = int((screen_width - window_width) // 2)
l = int((screen_height - window_height) // 4)
myroot.geometry(f"{window_width}x{window_height}+{w}+{l}")
myroot.iconbitmap("v6_2.ico")

lb1= Label(myroot,font=("Arial Bold",16),text="Информация об авторе программы")
lb1.grid(row=0,column=1)
y = Image.open("info.png")
y.thumbnail((50,50))
y1 = ImageTk.PhotoImage(y)
foto = Label(myroot, image=y1,borderwidth=0)
foto.grid(row=0,column=0,padx=5,pady=5)


m = Image.open("me.jpg")
m.thumbnail((200,200))
m1 = ImageTk.PhotoImage(m)
foto1 = Label(myroot, image=m1,borderwidth=0)
foto1.grid(row=1,column=1)

lb2= Label(myroot,font=("Arial Bold",16),text="Студент Международного \n"
                                            "Университета Кыргызстана")
lb2.grid(row=2,column=1)

p = Image.open("v6_2.ico")
p.thumbnail((50,50))
p1 = ImageTk.PhotoImage(p)
foto2 = Label(myroot, image=p1,borderwidth=0)
foto2.grid(row=2,column=0,padx=5,pady=5)

lb3 = Label(myroot,font=("Arial Bold",16),text="Работа выполнена в качестве \n"
                                             "курсовой работы")
lb3.grid(row=3,column=1)

lb5 = Label(myroot,font=("Arial Bold",16),text="Ссылки для контакта:")
lb5.grid(row=4,column=1)

lb6 = Label(myroot,font=("Arial Bold Italic",16),text="uulukmyrza27@gmail.com", fg="blue", cursor="hand2")
lb6.grid(row=5,column=1)
lb6.bind("<Button-1>", lambda  event: send_email())

lb7 = Label(myroot,font=("Arial Bold Italic",16),text="Telegram", fg="blue", cursor="hand2")
lb7.grid(row=6,column=1)
lb7.bind("<Button-1>", lambda  event: open_tg())

link_label = Label(myroot,font=("Arial Bold Italic",16), text="Github/NomadUluk", fg="blue", cursor="hand2")
link_label.grid(row=7,column=1)
link_label.bind("<Button-1>", lambda  event: open_git())

lb4 = Label(myroot,font=("Arial Bold",16),text="Все права принадлежат автору!")
lb4.grid(row=8,column=1)
def open_git():
    webbrowser.open("https://github.com/NomadUluk")
def send_email():
    webbrowser.open("mailto:example@example.com")
def open_tg():
    webbrowser.open("https://t.me/uluk_uzakbaev")

myroot.bind("<Escape>", lambda event: myroot.quit())
myroot.mainloop()