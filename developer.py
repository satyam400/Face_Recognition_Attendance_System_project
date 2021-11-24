from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="blue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)  #just place on background image

        img_top=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\developer.jfif")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)  #resize of image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)  #create label
        f_lbl.place(x=0,y=55,width=1530,height=730) #to show the image on window


        #================frame============
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_top1=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\satyam.p.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)  #resize of image
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)  #create label
        f_lbl.place(x=300,y=0,width=200,height=200) #to show the image on window

        #==============developer info================
        dev_label=Label(main_frame,text="hello my name is Satyam",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="i am full stack Developer",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\student.jpg")
        img2=img2.resize((500,390),Image.ANTIALIAS)  #resize of image
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)  #create label
        f_lbl.place(x=0,y=210,width=500,height=390) #to show the image on window


#create object
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()