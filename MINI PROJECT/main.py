from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognisation_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNISATION SYSTEM")

        #first image
        img = Image.open(r"C:\Users\akhil\OneDrive\Documents\MINI PROJECT\college_images\7new.JPG")
        img = img.resize((500,130),resample=Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=130)

        #second image
        img2 = Image.open(r"C:\Users\akhil\OneDrive\Documents\MINI PROJECT\college_images\7new.JPG")
        img2 = img2.resize((500,130),resample=Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root,image=self.photoimg2)
        first_label.place(x=500,y=0,width=500,height=130)

        #third image
        img3 = Image.open(r"C:\Users\akhil\OneDrive\Documents\MINI PROJECT\college_images\7new.JPG")
        img3 = img3.resize((550,130),resample=Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root,image=self.photoimg3)
        first_label.place(x=1000,y=0,width=550,height=130)

        #bg image
        img4 = Image.open(r"C:\Users\akhil\OneDrive\Documents\MINI PROJECT\college_images\bg.JPG")
        img4 = img4.resize((1530,710),resample=Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNISATION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student detail button
        b1 = Button(bg_img,text="STUDENT \n DETAILS",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=50,y=400,width=150,height=150)

        #face detector button
        b1 = Button(bg_img,text="FACE \n DETECTOR",cursor="hand2",font=("times new roman",19,"bold"),bg="light blue",fg="black")
        b1.place(x=250,y=400,width=150,height=150)

        #attendance button
        b1 = Button(bg_img,text="ATTEND- \n ANCE",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=450,y=400,width=150,height=150)

        #train face button
        b1 = Button(bg_img,text="TRAIN \n FACE",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=650,y=400,width=150,height=150)

        #photos button
        b1 = Button(bg_img,text="PHOTOS",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=850,y=400,width=150,height=150)

        #developer button
        b1 = Button(bg_img,text="STUDENT \n DETAILS",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=1050,y=400,width=150,height=150)

        #exit button
        b1 = Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        b1.place(x=1250,y=400,width=150,height=150)





if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognisation_System(root)
    root.mainloop()