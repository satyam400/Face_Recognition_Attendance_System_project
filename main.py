from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face Recognition System")
        
        #take the image from file
        #first image
        img=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\download (2).jfif")
        img=img.resize((500,130),Image.ANTIALIAS)  #resize of image
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)  #create label
        f_lbl.place(x=0,y=0,width=525,height=130) #to show the image on window


        #take the image from file
        #second image
        img1=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\download (1).jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)  #resize of image
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)  #create label
        f_lbl.place(x=500,y=0,width=525,height=130) #to show the image on window


        #take the image from file
        #third image
        img2=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\download.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)  #resize of image
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)  #create label
        f_lbl.place(x=1000,y=0,width=525,height=130) #to show the image on window


        #take the image from file
        #background image
        img3=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\future-bordern-face.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)  #resize of image
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)  #create label
        bg_img.place(x=0,y=130,width=1530,height=790) #to show the image on window

        #title of project
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="gray",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)  #just place on background image


        #student button
        img4=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2") #first button
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b1_1.place(x=200,y=320,width=220,height=40)


        
        #detect face button
        img5=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\FACE_DETECTOR.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2") #first button
        b2.place(x=500,y=100,width=220,height=220)

        b2_2=Button(bg_img,text="FACE DETECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b2_2.place(x=500,y=320,width=220,height=40)

        
       
        #attendance button
        img6=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2") #first button
        b3.place(x=800,y=100,width=220,height=220)

        b3_3=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b3_3.place(x=800,y=320,width=220,height=40)



        #help button
        img7=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\help.jfif")
        img7=img7.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2") #first button
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4=Button(bg_img,text="HELP DESK",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b4_4.place(x=1100,y=320,width=220,height=40)



        #train button
        img8=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\train data.jfif")
        img8=img8.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2") #first button
        b5.place(x=200,y=400,width=220,height=220)

        b5_5=Button(bg_img,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b5_5.place(x=200,y=620,width=220,height=40)



        #photos button
        img9=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img) #first button
        b6.place(x=500,y=400,width=220,height=220)

        b6_6=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b6_6.place(x=500,y=620,width=220,height=40)



        #developer button
        img10=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\developer.jfif")
        img10=img10.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2") #first button
        b7.place(x=800,y=400,width=220,height=220)

        b7_7=Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b7_7.place(x=800,y=620,width=220,height=40)




        #exit button
        img11=Image.open(r"C:\Users\SATYAM\Desktop\face_recognition_app\image\exit.jfif")
        img11=img11.resize((220,220),Image.ANTIALIAS)  #resize of image
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2") #first button
        b8.place(x=1100,y=400,width=220,height=220)

        b8_8=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="black") #text on first button
        b8_8.place(x=1100,y=620,width=220,height=40)


    #================just open photos of sample================
    def open_img(self):
        os.startfile("data")

    #===============function button for student details================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)





#create object
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
