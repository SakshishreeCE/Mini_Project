from tkinter import*
from tkinter import ttk, Canvas
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
from time import strftime
from tkinter.simpledialog import askstring
from tkinter import Tk, simpledialog
from datetime import datetime
import cv2
import os
import numpy as np  #pip install numpy
from datetime import timedelta

class Face_recognisation_system:
    # Dictionary to store the last entry time for each student
    last_entry_times = {}

    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),fg="white",bg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"imageskafile/faceme.JPG")
        img_top=img_top.resize((1530,790),resample=Image.BILINEAR)
        self.photoimage_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=790)

        b1 = Button(self.root,text="FACE RECOGNISATION",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="blue",fg="black")
        b1.place(x=300,y=420,width=1000,height=60)

    #============Attendence===================

    
    def mark_attendance(self, i, r, n, d, sub):
        csv_file_name = f"{sub}_Attendance.csv"
        # Define the time interval to consider for preventing duplicate entries (e.g., 15 minutes)
        interval = timedelta(minutes=15)
        
        # Check if the CSV file exists, if not create it with headers
        if not os.path.exists(csv_file_name):
            with open(csv_file_name, "w", newline="\n") as f:
                f.write("Student ID,Roll,Name,Department,Time,Date,Status\n")
        
        # Check if there is no entry for the student in the past 15 minutes
        now = datetime.now()
        last_entry_time = self.last_entry_times.get((i, r, n, d, sub), None)
        if last_entry_time is not None and now - last_entry_time <= interval:
            # If there is an entry within the last 15 minutes, return without adding a new entry
            return
        
        # If there is no entry for the student in the past 15 minutes, add the new entry
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
        new_entry = f"{i},{r},{n},{d},{dtString},{d1},Present\n"
        with open(csv_file_name, "a", newline="\n") as f:  # Open in append mode
            f.write(new_entry)
        
        # Update the last entry time for the student
        self.last_entry_times[(i, r, n, d, sub)] = now






    #=========face recognisation ===============
    def face_recog(self):
        subject_name = simpledialog.askstring("Input", "Please enter the subject name:", parent=self.root)
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Ram1234*", database="face_recognizer")     
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT student_id FROM student_data WHERE student_id = %s", (id,))
                i=my_cursor.fetchone()
                i="+".join(i)

                # # my_cursor.execute("SELECT name FROM student_data WHERE student_id ",str(id))
                my_cursor.execute("SELECT name FROM student_data WHERE student_id = %s", (id,))
                n=my_cursor.fetchone()
                # print("test...",id,predict)
                n="+".join(n)

                # my_cursor.execute("SELECT roll FROM student_data WHERE student_id ",str(id))
                my_cursor.execute("SELECT roll FROM student_data WHERE student_id = %s", (id,))
                r=my_cursor.fetchone()
                r="+".join(r)

                # my_cursor.execute("SELECT dept FROM student_data WHERE student_id ",str(id))
                my_cursor.execute("SELECT dept FROM student_data WHERE student_id = %s", (id,))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence > 77:
                    # cv2.putText(img,f"ID:{i}\n",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d,subject_name)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0.255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognisation",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__=="__main__":
    root=Tk()
    obj=Face_recognisation_system(root)
    root.mainloop()