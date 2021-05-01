from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import pymysql
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Welcome to Student Details")

        images = Image.open("images/trainf"
                            ".png")
        images = images.resize((1500, 900), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(images)
        bg11 = Label(self.root, image=self.bg11).place(x=0, y=0, relwidth=1, relheight=1)



        button1 = Button(self.root, command=self.trainclassifier, text="Train Images", cursor="hand2",
                         font=("comic sans", 25, "bold"), fg="royal blue", highlightbackground="white")
        button1.place(x=105, y=600, width=220, height=40)

        button2 = Button(self.root, command=self.face_rec, text="Exit", cursor="hand2",
                         font=("comic sans", 25, "bold"), fg="royal blue", highlightbackground="red")
        button2.place(x=105, y=650, width=150, height=25)

    def trainclassifier(self):
        datadir=("/Users/kaivanvisaria/PycharmProjects/miniproj/login_database/DATA")
        path=[os.path.join(datadir,file)for file in os.listdir(datadir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imgNp=np.array(img,'uint8')

            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training",imgNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Message","Training datasets completed")

    def face_rec(self):
        self.root.destroy()
        import facerecognizer









root=Tk()
obj=Train(root)
root.mainloop()