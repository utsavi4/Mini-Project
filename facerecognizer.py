from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import pymysql
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Facerecognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Welcome")

        images = Image.open("images/facialrec1.png")
        images = images.resize((1500, 900), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(images)
        bg11 = Label(self.root, image=self.bg11).place(x=0, y=0, relwidth=1, relheight=1)



        button1 = Button(self.root,command=self.recognition, text="Get Started", cursor="hand2",
                         font=("comic sans", 25, "bold"), fg="royal blue", highlightbackground="white")
        button1.place(x=275, y=570, width=220, height=40)

        button2 = Button(self.root, command=self.check_attendance, text="Check your Attendance", cursor="hand2",
                         font=("comic sans", 20, "bold"), fg="white", highlightbackground="red")
        button2.place(x=275, y=620, width=250, height=30)

        #attendance

    def mark_attendance(self,i,n,d,e):
        with open("/Users/kaivanvisaria/PycharmProjects/miniproj/login_database/Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list) and (e not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{e},{dtString},{d1},Present")

    def check_attendance(self):
        self.root.destroy()
        import MarkAttendance






    def recognition(self):

        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                       database="face-recognition")
                cur = conn.cursor()
                cur.execute("select name from student where ID=" + str(id))
                n = cur.fetchone()
                n = "+".join(n)

                cur.execute("select ID from student where ID=" + str(id))
                i = cur.fetchone()
                i = "+".join(i)



                cur.execute("select department from student where ID=" + str(id))
                d = cur.fetchone()
                d = "+".join(d)

                cur.execute("select email from student where ID=" + str(id))
                e = cur.fetchone()
                e = "+".join(e)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    cv2.putText(img, f"name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"department:{d}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"email:{e}", (x, y-15 ), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,n,d,e)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognisation(img,clf,faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap = cv2.VideoCapture(0)

        while True:
            ret, img = videocap.read()
            img = recognisation(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognisation", img)

            if cv2.waitKey(1) == 13:
                break

        videocap.release()
        cv2.destroyAllWindows()


root=Tk()
obj=Facerecognizer(root)
root.mainloop()

