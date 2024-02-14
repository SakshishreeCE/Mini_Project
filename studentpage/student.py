from tkinter import*
from tkinter import ttk, Canvas
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        
        #first image
        img=Image.open(r"imageskafile/student1.jpg")
        img=img.resize((400,180),resample=Image.BILINEAR)
        self.photoimage=ImageTk.PhotoImage(img)
        
        f_lbl=Label(image=self.photoimage,borderwidth=0)
        f_lbl.place(x=0,y=0,width=400,height=180)

        #second image
        img1=Image.open(r"imageskafile/registerbg.jpg")
        img1=img1.resize((400,180),resample=Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(image=self.photoimage1,borderwidth=0)
        f_lbl.place(x=500,y=0,width=400,height=180)
        

        #third image
        img2=Image.open(r"imageskafile/student2.jpg")
        img2=img2.resize((400,180),resample=Image.BILINEAR)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(image=self.photoimage2,borderwidth=0)
        f_lbl.place(x=1000,y=0,width=400,height=180)
        

        #bg image
        img3=Image.open(r"imageskafile/studentbg.jpg")
        img3=img3.resize((1530,710),resample=Image.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=180,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=45,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        #img_left=Image.open(r"C:\Users\Rashmi Papnoi\Desktop\TY\studentpage\images\left.jpg")
        #img_left=img_left.resize((400,130),Image.ANTIALIAS)
        #self.photoimage_left=ImageTk.PhotoImage(img_left)

        #f_lbl=Label(Left_frame,image=self.photoimage_left)
        #f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=5,width=720,height=115)
        
        #department
        dep_label=Label(current_course,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","CST","IT","DS","ENC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","NNDL","MAM","AI","CD","CN")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-24","2021-25","2022-26","2023-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        Semester_combo["values"]=("Select Semester","Semester 2","Semester 4","Semester 6","Semester 8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=115,width=720,height=300)

        #student id
        studentId_label=Label(class_student,text="StudentID",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studeName_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        studeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class division
        class_div_label=Label(class_student,text="Class Division",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        rollno_label=Label(class_student,text="Roll No.",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student,text="Email",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone
        phone_label=Label(class_student,text="Phone",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_student,text="Address",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label=Label(class_student,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        radiobtn1=ttk.Radiobutton(class_student,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=1)

        radiobtn2=ttk.Radiobutton(class_student,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=5,column=2)

        #buttons frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="white",fg="black")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="white",fg="black")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="white",fg="black")
        Reset_btn.grid(row=0,column=3)

        #another button frame
        btn_frame1=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        Take_btn=Button(btn_frame1,text="Take Photo Sample",width=34,font=("times new roman",13,"bold"),bg="white",fg="black")
        Take_btn.grid(row=0,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=34,font=("times new roman",13,"bold"),bg="white",fg="black")
        updatephoto_btn.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        img_right=Image.open(r"imageskafile/right.jpg")
        img_right=img_right.resize((720,180),resample=Image.BILINEAR)
        self.photoimage_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimage_right)
        f_lbl.place(x=5,y=0,width=720,height=180)

        #Search System
        search_student=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_student.place(x=5,y=180,width=710,height=70)

        search_label=Label(search_student,text="Search By:",font=("times new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_student,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_student,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_student,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="black")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_student,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="black")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_student=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_student.place(x=5,y=255,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_student,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_student,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_student,column=("dep","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)






if __name__=="__main__":
    root=Tk()
    app=Student(root)
    root.mainloop()