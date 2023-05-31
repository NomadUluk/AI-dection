import pixellib
from imageai.Detection import VideoObjectDetection
from pixellib.torchbackend.instance import instanceSegmentation
import cv2
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import os
import subprocess

def main():
    global picture , myWindow
    picture = ""
    myWindow = Tk()
    myWindow.title("Нейросетевая система распознавания")
    # myWindow.geometry('600x600')
    screen_width = myWindow.winfo_screenwidth()
    screen_height = myWindow.winfo_screenheight()
    window_width = 600
    window_height = 620
    w = int((screen_width - window_width) // 2)
    l = int((screen_height - window_height) //4)
    myWindow.geometry(f"{window_width}x{window_height}+{w}+{l}")
    myWindow.iconbitmap("v6_2.ico")

    foto = Frame(myWindow)
    foto.pack(side=TOP)
    frame = Frame(myWindow)
    frame.pack()
    button1 = Button(frame,text="Выбрать изображение", command=open_file,relief="solid",
                     background='red', foreground='white', font=('Arial', 14),
                     activebackground="grey",activeforeground="red",cursor="plus")
    button1.pack(padx=5,pady=5)
    global button2
    button2 = Button(frame,text="Распознать обьекты на изображении",state=NORMAL, command=button_click,relief="solid",
                     background='red', foreground='white', font=('Arial', 14),
                     activebackground="grey",activeforeground="red",cursor="dotbox")
    button2.pack(padx=5,pady=5)
    button3 = Button(frame, text="Распознать объекты на видео", command=open_video,relief="solid",
                     background='red', foreground='white', font=('Arial', 14),
                     activebackground="grey",activeforeground="red",cursor="plus")
    button3.pack(padx=5,pady=5)
    button4 = Button(frame, text="В реальном времени", command=online,relief="solid",
                     background='red', foreground='white', font=('Arial', 14),
                     activebackground="grey",activeforeground="red",cursor="clock")
    button4.pack(padx=5,pady=5)
    global answer
    answer = Label(frame,text="",font=("Arial Bold",14),fg="white",borderwidth=5)
    answer.pack(pady=5)
    global lb2
    lb2 = Label(foto, text="Нейросетевая система распознавания",font=("Arial Bold",16),
                fg="white",bg="#FE0000",relief="raised")
    lb2.pack(pady=5)
    global lb1
    y = Image.open("logo.png")
    y.thumbnail((560,450))
    y1 = ImageTk.PhotoImage(y)
    lb1 = Label(foto, image=y1,relief="ridge",pady=15)
    lb1.pack()

    menu = Menu(myWindow)

    help_menu = Menu(menu,tearoff=False)
    menu.add_command(label="Помощь (F1)",command=open_help)
    menu.add_separator()
    menu.add_command(label="О программе (F2)", command=open_version)
    menu.add_separator()
    menu.add_command(label="Об авторе (F3)", command=open_about)

    myWindow.bind("<Escape>", lambda event: myWindow.quit())
    myWindow.bind("<F1>",lambda event: open_help())
    myWindow.bind("<F2>", lambda event: open_version())
    myWindow.bind("<F3>", lambda event: open_about())

    myWindow.configure(menu = menu)
    myWindow.mainloop()

def button_click():
    if picture != "":
        findimage(picture)
    else:
        answer.config(text="Пожалуйста выберите изображение!",bg="#FFD700",fg="black")
        button2.config(state=DISABLED)

def open_file():
    global picture
    filename = askopenfilename(filetypes=[("All Files", "*.*")])
    picture = os.path.basename(filename)
    image = Image.open(filename)
    image.thumbnail((550, 300))
    image_tk = ImageTk.PhotoImage(image)
    lb1.config(image=image_tk)
    lb1.image = image_tk
    button2.config(state=NORMAL)
    answer.config(text="Отлично, вы выбрали! Начнем?", bg="#FF0800",fg="white")

def open_video():
    global picture
    answer.config(text="Отлично, выберите и ожидайте!", bg="#FF0800",fg="white")
    filename = askopenfilename(filetypes=[("MP4 videos", "*.mp4")])
    picture = os.path.basename(filename)
    if picture == "":
        answer.config(text="Файл не выбран!",bg="#FFD700",fg="black")
    else:
        findvideo(picture)
        answer.config(text="Обработка произошла успешно!", bg="#00BB00")



def online():
    capture = cv2.VideoCapture(0)
    capture.set(3,1920)
    capture.set(4,1080)
    segment_video = instanceSegmentation()
    segment_video.load_model("pointrend_resnet50.pkl", confidence= 0.7, detection_speed="fast")
    segment_video.process_camera(capture, show_bboxes=True, frames_per_second=2,
                                text_size = 1,frame_name ="Online", output_video_name="online.mp4",
                                 box_thickness=1,text_thickness=2)
    os.startfile("online.mp4")

def findimage(picture):
    ins = instanceSegmentation()
    ins.load_model("pointrend_resnet50.pkl")
    result = ins.segmentImage(picture, show_bboxes=True, output_image_name="output_image.jpg",
                     text_thickness=2, box_thickness=1, segment_target_classes=None,text_size=0.8)
    objects_count = len(result[0]["scores"])
    x = Image.open("output_image.jpg")
    x.thumbnail((560, 300))
    x1 = ImageTk.PhotoImage(x)
    lb1.config(image=x1 , justify="center")
    lb1.image = x1
    answer.config(text=f"Обработка произошла успешно!\n"
                       f"Найдено обьектов: {objects_count}", bg="#00BB00")
    os.startfile("output_image.jpg")

def findvideo(picture):
    global exec_path
    exec_path = os.getcwd()
    vids = VideoObjectDetection()
    vids.setModelTypeAsYOLOv3()
    vids.setModelPath( os.path.join(exec_path ,"yolov3.pt"))
    vids.loadModel()
    result= vids.detectObjectsFromVideo(input_file_path=os.path.join(exec_path, picture),
                            output_file_path=os.path.join(exec_path, "detected")
                            , frames_per_second=10,log_progress=True,frame_detection_interval=2)
    os.startfile("detected.mp4")

    # ins = instanceSegmentation()
    # ins.load_model("pointrend_resnet50.pkl", detection_speed="fast")
    # ins.process_video(picture, show_bboxes=True, frames_per_second=24, output_video_name="output_video.mp4")
def open_help():
    subprocess.run(['python', "helpWindow.py"])

def open_version():
    subprocess.run(['python', "version.py"])

def open_about():
        subprocess.run(['python', "about.py"])

if __name__ == '__main__':
    main()