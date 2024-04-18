from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognisation_system
from attendance import Attendance


class Face_Recognisation_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        #first image
        img = Image.open(r"imageskafile/studentbg.JPG")
        img = img.resize((500,130),resample=Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=130)

        #second images
        img2 = Image.open(r"imageskafile/studentbg.JPG")
        img2 = img2.resize((500,130),resample=Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root,image=self.photoimg2)
        first_label.place(x=500,y=0,width=500,height=130)

        #third image
        img3 = Image.open(r"imageskafile/studentbg.JPG")
        img3 = img3.resize((550,130),resample=Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root,image=self.photoimg3)
        first_label.place(x=1000,y=0,width=550,height=130)

        #bg image
        img4 = Image.open(r"imageskafile/left.JPG")
        img4 = img4.resize((1530,710),resample=Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student detail button
        b1 = Button(bg_img,text="STUDENT \n DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=50,y=300,width=200,height=200)

        #face detector button
        b1 = Button(bg_img,text="FACE \n DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",19,"bold"),bg="light blue",fg="black")
        b1.place(x=300,y=300,width=200,height=200)

        #attendance button
        b1 = Button(bg_img,text="ATTEND- \n ANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=550,y=300,width=200,height=200)

        #train face button
        b1 = Button(bg_img,text="TRAIN \n FACE",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=800,y=300,width=200,height=200)

        #photos button
        b1 = Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=1050,y=300,width=200,height=200)

        #developer button
        # b1 = Button(bg_img,text="DEVE\nLOPER",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        # b1.place(x=1050,y=400,width=150,height=150)

        #exit button
        b1 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=1300,y=300,width=200,height=200)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit ",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

# ============================================Functions buttons=======================
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)

    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_recognisation_system(self.new_window)

    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognisation_System(root)
    root.mainloop()