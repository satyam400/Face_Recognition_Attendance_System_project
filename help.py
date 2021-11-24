from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face Recognition System")



        

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)  #just place on background image

        img_top=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\HELP DESK.JPG")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)  #resize of image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)  #create label
        f_lbl.place(x=0,y=55,width=1530,height=730) #to show the image on window

        


        dev_label=Label(f_lbl,text="Email:satyam.gla_cs19@gla.ac.in",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=260)


#create object
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()