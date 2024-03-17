from tkinter import*
from tkinter import ttk, Canvas
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
from register import Register
from main import Face_Recognisation_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"imageskafile/studentbg.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"imageskafile/login.jpg")
        img1 = img1.resize((100,100),resample=Image.BILINEAR)
        
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(image=self.photoimage1,borderwidth=0)
        lbling1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon Images
        img2=Image.open(r"imageskafile/login.jpg")
        img2 = img2.resize((25,25),resample=Image.BILINEAR)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"imageskafile/pw.jpg")
        img3 = img3.resize((25,25),resample=Image.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbling1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbling1.place(x=650,y=395,width=25,height=25)

        #loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassbutton
        forgetpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="rashmi" and self.txtpass.get()=="rash":
            messagebox.showinfo("Success","Welcome!")
        else:
            conn=mysql.connector.connect(host="localhost",user="user",password="Ram1234*",database="login")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognisation_System(self.new_window)
                    self.new_window.mainloop()
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


#################################reset password#############################################
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select a security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ram1234*",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with the new password",parent=self.root2)
                self.root2.destroy()

        
##################################forgot password window#################################################            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter your email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ram1234*",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x451+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1,)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="randomly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet name","Your favourite fruit")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpassword.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15),fg="white",bg="red")
                btn.place(x=100,y=290)
    

            








if __name__=="__main__":
    main()