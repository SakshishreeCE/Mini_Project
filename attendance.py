from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("face Recognition System")
         
         #variables
         self.var_atten_id=StringVar()
         self.var_atten_roll=StringVar()
         self.var_atten_name=StringVar()
         self.var_atten_dep=StringVar()
         self.var_atten_time=StringVar()
         self.var_atten_date=StringVar()
         self.var_atten_attendance=StringVar()
         
         #first Image
         img=Image.open(r"imageskafile/studentbg.jpg")
         img=img.resize((1530,710),resample=Image.BILINEAR)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=800,height=200)
         
         #Second Image
         img1=Image.open(r"imageskafile/studentbg.jpg")
         img1=img1.resize((1530,710),resample=Image.BILINEAR)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=800,y=0,width=800,height=200)
         
        #bgImage
         img3=Image.open(r"imageskafile/studentbg.jpg")
         img3=img3.resize((1530,710),resample=Image.BILINEAR)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_image=Label(self.root,image=self.photoimg3)
         bg_image.place(x=0,y=200,width=1530,height=710)
         
         title_lbl=Label(bg_image,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Playfair Display",35,"bold"),bg="DarkGoldenRod3",fg="Blue4")
         title_lbl.place(x=0,y=0,width=1530,height=45)
         
         main_frame=Frame(bg_image,bd=2,bg="white")
         main_frame.place(x=10,y=55,width=1500,height=600)
         
         # left label frame
         Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
         Left_frame.place(x=10,y=10,width=760,height=580)
         
         img_left=Image.open(r"imageskafile/studentbg.jpg")
         img_left=img_left.resize((1530,710),resample=Image.BILINEAR)
         self.photoimg_left=ImageTk.PhotoImage(img_left)
         
         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=745,height=130)
         
         Left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
         Left_inside_frame.place(x=5,y=135,width=740,height=370)
         
         #labels and entry
         
         # Attendance ID
         attendance_label=Label(Left_inside_frame,text="Attendance Id:",font=("times new roman",12,"bold"),bg="white")
         attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         attendance_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
         attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         
         # Roll
         Roll_label=Label(Left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
         Roll_label.grid(row=0,column=2,padx=4,pady=8)

         atten_roll=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
         atten_roll.grid(row=0,column=3,pady=8)
         
         # Name
         Name_label=Label(Left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
         Name_label.grid(row=1,column=0)

         atten_name=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
         atten_name.grid(row=1,column=1,pady=8)
         
         # Department
         Dep_label=Label(Left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
         Dep_label.grid(row=1,column=2)

         atten_dep=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
         atten_dep.grid(row=1,column=3,pady=8)
         
         # Time
         Time_label=Label(Left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
         Time_label.grid(row=2,column=0)

         atten_time=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
         atten_time.grid(row=2,column=1,pady=8)
         
         # Date
         Date_label=Label(Left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
         Date_label.grid(row=2,column=2)

         atten_date=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
         atten_date.grid(row=2,column=3,pady=8)
         
         # Attendance_Status
         Attendance_Status_label=Label(Left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
         Attendance_Status_label.grid(row=3,column=0)

         self.atten_status=ttk.Combobox(Left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman", 12,"bold"))
         self.atten_status["values"]=("Status","Present","Absent")
         self.atten_status.grid(row=3,column=1,pady=8)
         self.atten_status.current(0)
         
         #buttons Frame
         btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=10,y=250,width=715,height=35)

         Import_CSV_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=18,font=("times new roman",12,"bold"))
         Import_CSV_btn.grid(row=0,column=0)

         Exprt_CSV_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=18,font=("times new roman",12,"bold"))
         Exprt_CSV_btn.grid(row=0,column=1)

         Update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"))
         Update_btn.grid(row=0,column=2)

         Reset_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",12,"bold"))
         Reset_btn.grid(row=0,column=3)
         
         # right label frame
         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))                      
         Right_frame.place(x=750,y=10,width=720,height=580)
         
         table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=5,y=5,width=700,height=455)
         
         #Scroll Bar
         
         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
         
         self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         
         scroll_x.config(command=self.AttendanceReportTable.xview)
         scroll_y.config(command=self.AttendanceReportTable.yview)
         
         self.AttendanceReportTable.heading("id",text="Attendance ID")
         self.AttendanceReportTable.heading("roll",text="Roll")
         self.AttendanceReportTable.heading("name",text="Name")
         self.AttendanceReportTable.heading("department",text="Department")
         self.AttendanceReportTable.heading("time",text="Time")
         self.AttendanceReportTable.heading("date",text="Date")
         self.AttendanceReportTable.heading("attendance",text="Attendance")
         
         self.AttendanceReportTable["show"]="headings"
         
         self.AttendanceReportTable.column("id",width=100)
         self.AttendanceReportTable.column("roll",width=100)
         self.AttendanceReportTable.column("name",width=100)
         self.AttendanceReportTable.column("department",width=100)
         self.AttendanceReportTable.column("time",width=100)
         self.AttendanceReportTable.column("date",width=100)
         self.AttendanceReportTable.column("attendance",width=100)
         
         
         self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         
         self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
         
#==================Fetch data=======================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
            
            
            
 #Import CSV           
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
 #Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+  os.path.basename(fln)+ " Succesfully")
        except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
                 
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])      
        
    def reset_data(self):  
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")      
        
         
         
         
         
if __name__== "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop() 