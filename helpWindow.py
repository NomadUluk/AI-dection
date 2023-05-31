from tkinter import *
from PIL import ImageTk, Image

helpWindow = Tk()
helpWindow.title("Окно помощи для пользователя!")
screen_width = helpWindow.winfo_screenwidth()
screen_height = helpWindow.winfo_screenheight()
window_width = 400
window_height = 250
w = int((screen_width - window_width) // 2)
l = int((screen_height - window_height) // 4)
helpWindow.geometry(f"{window_width}x{window_height}+{w}+{l}")
helpWindow.iconbitmap("v6_2.ico")

y = Image.open("info.png")
y.thumbnail((50,50))
y1 = ImageTk.PhotoImage(y)
foto = Label(helpWindow, image=y1,borderwidth=0)
foto.pack(side=TOP,pady=5)
lb1= Label(helpWindow,font=("Aria Bold",14),text="* Это окно помощи для программы "
                                                 "\n'Нейросетевая система распознования'!\n").pack(side=TOP)
lb2= Label(helpWindow,font=("Arial Bold",12),text="* нажмите 'F1' чтобы вызвать окно помощи.").pack(fill=BOTH)
lb3 = Label(helpWindow,font=("Arial Bold",12),text="* нажмите 'F2' чтобы узнать об программе.").pack(fill=BOTH)
lb4 = Label(helpWindow,font=("Arial Bold",12),text="* нажмите 'F3' чтобы узнать об авторе.").pack(fill=BOTH)
lb5 = Label(helpWindow,font=("Arial Bold",12),text="* нажмите 'Esc' чтобы закрыть окно.").pack(fill=BOTH)
helpWindow.bind("<Escape>",lambda event: helpWindow.quit())
helpWindow.mainloop()