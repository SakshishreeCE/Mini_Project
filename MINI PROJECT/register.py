from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #--------------variables------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #------------------background----------------------------
         # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Resize the image to cover the whole screen
        bg_image = Image.open(r"imageskafile/registerbg.jpg")
        resized_bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(resized_bg_image)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         #------------------left----------------------------------
        self.bg1=ImageTk.PhotoImage(file=r"imageskafile/left.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #------------------frame---------------------------------
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue",bg="white")
        register_lbl.place(x=20,y=20)

         #------------------label---------------------------------
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

         #-----------------row2------------------------------------
        contact=Label(frame,text="Contact:",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email id:",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #----------------row3-------------------------------------
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="randomly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet name","Your favourite fruit")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #-----------------row4-----------------------------------
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Comfirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #----------------checkbtn--------------------------------
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree with the terms and conditons",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #-----------------buttons------------
        img=Image.open(r"imageskafile/registration-button.jpg" )
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",18,"bold"),fg="white")
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"imageskafile/loginnow.jpg" )
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",18,"bold"),fg="white")
        b1.place(x=330,y=420,width=300)

    
    #--------------Function Declaration--------------------
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
       # elif self.var_pass.get!=self.var_confpass.get():
        #    messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree with the terms and conditions.")
        else:
            conn=mysql.connector.connect(host="localhost",user="rashmi",password="123456",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists. Please use another email.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()   
            messagebox.showinfo("Success!","Registered Successfully!")


#####################################################################################
    def return_login(self):
        self.root.destroy()




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()