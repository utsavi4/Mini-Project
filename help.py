from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import pymysql
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Facial Recognition Attendance System")

        mainframe = Frame(self.root, bd=2, bg="black")
        mainframe.place(x=20, y=55, width=1400, height=700)

root=Tk()
obj=Help(root)
root.mainloop()
