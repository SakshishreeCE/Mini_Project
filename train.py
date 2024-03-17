from tkinter import*
from tkinter import ttk, Canvas
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np  #pip install numpy

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),fg="white",bg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"imageskafile/7new.JPG")
        img_top=img_top.resize((1530,325),resample=Image.BILINEAR)
        self.photoimage_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)


        b1 = Button(self.root,text="TRAIN ME",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="black")
        b1.place(x=0,y=380,width=1530,height=60)


        img_bottom=Image.open(r"imageskafile/bg.JPG")
        img_bottom=img_bottom.resize((1530,325),resample=Image.BILINEAR)
        self.photoimage_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimage_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Trainng",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        # =============== Train the classifier And save =====================
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


        


            
            


        






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()