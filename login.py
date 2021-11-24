from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\login_bg.jpg")
        img1=img1.resize((1550,800),Image.ANTIALIAS)

        self.bg=ImageTk.PhotoImage(img1)
        lbl_bg=Label(self.root,image=self.bg)
     
        lbl_bg.place(x=1,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img2=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\login_face.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=730,y=175,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #lebels
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)


        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        #==============icon images=============
        img3=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\login_face.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=323,width=25,height=25)

        img4=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\password.png")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lbl_img4=Label(image=self.photoimage4,bg="black",borderwidth=0)
        lbl_img4.place(x=650,y=400,width=25,height=25)
        

        #==============login btn========
        login_button=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=300,width=120,height=35)

        #========register btn=============
        register_button=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_button.place(x=15,y=350,width=160)

        #==============forgot btn=========
        forgot_button=Button(frame,command=self.forgot_pass,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgot_button.place(x=10,y=370,width=160)

    #============register windw===========
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="41352":
            
            messagebox.showinfo("Success","welcome to Atumate Attendance System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="41352000",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()


            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("Yes No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()


    #============reset paaword======================
    def reset_password(self):
        if self.combosequrity_q.get()=="Select":
            messagebox.showerror("Error","Select the security question ",parent=self.root2)
        elif self.sequrity_a_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.text_new_pass.get()=="":
            messagebox.showerror("Error","please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="41352000",database="face_recognizer")
            my_cursor=conn.cursor()

            query=("select * from register where email=%s and sequrityQ=%s and sequrityA=%s")
            value=(self.txtuser.get(),self.combosequrity_q.get(),self.sequrity_a_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.text_new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()    

    #=================forgot password window=================
    def forgot_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Eror","Please enter the email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="41352000",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            

            if row == None:
                messagebox.showerror("Error","please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                sequrity_q=Label(self.root2,text="Sequrity Question",font=("times new roman",18,"bold"),bg="white")
                sequrity_q.place(x=50,y=80)

                self.combosequrity_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combosequrity_q["values"]=("Select","Your Birth Place","Your Girlfriencd name","Your Pet Name")
                self.combosequrity_q.place(x=50,y=110,width=250)
                self.combosequrity_q.current(0)

                sequrity_a=Label(self.root2,text="Sequrity Answer",font=("times new roman",18,"bold"),bg="white")
                sequrity_a.place(x=50,y=150)
                self.sequrity_a_entry=ttk.Entry(self.root2,font=("times new roman",18,"bold"))
                self.sequrity_a_entry.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman",18,"bold"),bg="white")
                new_pass.place(x=50,y=220)
                self.text_new_pass=ttk.Entry(self.root2,font=("times new roman",18,"bold"))
                self.text_new_pass.place(x=50,y=250,width=250)


                btn=Button(self.root2,command=self.reset_password,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1560x800+0+0")

        #===============variables===============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #==============bg image=============
        img1=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\register.jpg")
        img1=img1.resize((1550,800),Image.ANTIALIAS)

        self.bg=ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #======left image===========
        img2=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\left_image.jfif")
        img2=img2.resize((500,600),Image.ANTIALIAS)

        self.bg1=ImageTk.PhotoImage(img2)
        bg_lbl1=Label(self.root,image=self.bg1)
        bg_lbl1.place(x=50,y=100,width=470,height=550)
        
        #==========main frame============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #======label and entry fill===============

        #======================row 1===========
        fname=Label(frame,text="First name",font=("times new roman",18,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",18,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last name",font=("times new roman",18,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",18,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        #================row 2============
        contact=Label(frame,text="Contact no",font=("times new roman",18,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",18,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",18,"bold"),bg="white")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",18,"bold"))
        self.email_entry.place(x=370,y=200,width=250)

        #===========row 3========
        sequrity_q=Label(frame,text="Sequrity Question",font=("times new roman",18,"bold"),bg="white")
        sequrity_q.place(x=50,y=240)

        self.combosequrity_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combosequrity_q["values"]=("Select","Your Birth Place","Your Girlfriencd name","Your Pet Name")
        self.combosequrity_q.place(x=50,y=270,width=250)
        self.combosequrity_q.current(0)

        sequrity_a=Label(frame,text="Sequrity Answer",font=("times new roman",18,"bold"),bg="white")
        sequrity_a.place(x=370,y=240)
        self.sequrity_a_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",18,"bold"))
        self.sequrity_a_entry.place(x=370,y=270,width=250)

        #=============row 4============
        password=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="white")
        password.place(x=50,y=340)

        self.pasw_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",18,"bold"))
        self.pasw_entry.place(x=50,y=370,width=250)

        cnf_password=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),bg="white")
        cnf_password.place(x=370,y=340)

        self.cnf_password_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",18,"bold"))
        self.cnf_password_entry.place(x=370,y=370,width=250)


        #=============check btn============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms & Conditions ",font=("times new roman",15,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=420)


        #===========btns===============
        img=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\register_now.jfif")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage4,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=30,y=460,width=200)

        img1=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\login_now.jfif")
        img1=img1.resize((200,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=460,y=450,width=200)



    #============function declaration===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","all fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password doesnt match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="41352000",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist, please try another email")
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
            messagebox.showinfo("Success","Register Succesfully, thanks for being here")
    
    def return_login(self):
        self.root.destroy()




if __name__=="__main__":
    main()