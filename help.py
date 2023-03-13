import os
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from attendance import Attendance
from face_recognition import Face_Recognition
from student import Student
from train import Train


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Help Desk", font = ("Springtime - Personal Use", 40, "bold"),bg = "#3171b9", fg = "White")
        title_lbl.place(x=0,y=0,width=1530,height=60)



        #+++++++++TOP IMAGE++++++++++++++
        img_top = Image.open(r"Raw Images\Help Desk.jpg")
        img_top = img_top.resize((1530,730),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=1530,height=730)

        Help_label = Label(f_lbl, text="If any issues in the software Contact : krishkumawat634@gmail.com", font=("Contage Bold", 19, "bold"),bg="#f6fafd", foreground="#3171b9")
        Help_label.place(x=350,y=681)

        

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
