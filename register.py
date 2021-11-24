from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
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







if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()