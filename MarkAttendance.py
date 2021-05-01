from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import pymysql
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import mailfunction
import time

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Welcome to Attendance Page")


        images = Image.open("images/marka.png")
        images = images.resize((1500, 900), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(images)
        bg11 = Label(self.root, image=self.bg11).place(x=0, y=0, relwidth=1, relheight=1)


        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview",
                        background="#E0FFFF",
                        foreground="Red",
                        fieldbackground="#E0FFFF",
                        rowheight="35",
                        fieldforeground="Green")
        style.map('Treeview',background=[('selected', 'purple')])






        self.var_attid=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()

        self.var_date=StringVar()
        self.status=StringVar()






        insideframe = Frame(root, bd=0,relief=RIDGE, bg="#E0FFFF")
        insideframe.place(x=103, y=110, width=605, height=300)

        id_label2 = Label(self.root, text="Student Attendance Details", font=("times new roman", 25, "bold"),
                         highlightbackground="#E0FFFF", bg="#E0FFFF")
        id_label2.place(x=103,y=80,height=30,width=605)

        id_label = Label(insideframe, text="Attendance ID", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.id_entry = ttk.Entry(insideframe,textvariable=self.var_attid, width=10,
                                  font=("times new roman", 15, "bold"))
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        name_label = Label(insideframe, text="Date", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        self.name_entry = ttk.Entry(insideframe,textvariable=self.var_date, width=15,
                                  font=("times new roman", 15, "bold"))
        self.name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        date_label = Label(insideframe, text="Name of the Student", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        date_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.date_entry = ttk.Entry(insideframe, width=15,textvariable=self.var_name,
                                    font=("times new roman", 15, "bold"))
        self.date_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        time_label = Label(insideframe, text="Time", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        time_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        self.time_entry = ttk.Entry(insideframe, width=15,textvariable=self.var_time,
                                    font=("times new roman", 15, "bold"))
        self.time_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        dep_label = Label(insideframe, text="Department", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        dep_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.dep_entry = ttk.Entry(insideframe, width=15,textvariable=self.var_dep,
                                    font=("times new roman", 15, "bold"))
        self.dep_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        attendance_label = Label(insideframe, text="Attendance Status", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        attendance_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.attendance_combo = ttk.Combobox(insideframe,textvariable=self.status,
                                         font=("times new roman", 15, "bold"), width=15)
        self.attendance_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=4, column=1, padx=4, pady=10, sticky=W)

        email_label = Label(insideframe, text="Email ID", font=("times new roman", 15, "bold"),highlightbackground="#E0FFFF",bg="#E0FFFF")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.email_entry = ttk.Entry(insideframe, textvariable=self.var_email, width=25,
                                    font=("times new roman", 15, "bold"))
        self.email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        buttonframe = Frame(insideframe, relief=RIDGE,bg="#E0FFFF")
        buttonframe.place(x=0, y=200, width=600, height=80)


        savebtn = Button(buttonframe,command=self.importcsv, text="Import CSV", font=("times new roman", 15, "bold"),
                         highlightbackground="blue", fg="white", width="18")
        savebtn.grid(row=1, column=0)


        updatebtn = Button(buttonframe,command=self.exportcsv, text="Export CSV",  font=("times new roman", 15, "bold"),
                            highlightbackground="blue", fg="white", width="18")
        updatebtn.grid(row=1, column=1)


        deletebtn = Button(buttonframe, text="Update",command=self.update_data, font=("times new roman", 15, "bold"),
                           highlightbackground="blue",
                           fg="white", width="18")
        deletebtn.grid(row=1, column=2)


        resetbtn = Button(buttonframe,command=self.reset_data, text="Reset",  font=("times new roman", 15, "bold"),
                          highlightbackground="blue",
                          fg="white", width="18")
        resetbtn.grid(row=1, column=3)

        grpbtn = Button(buttonframe, text="Graph", font=("times new roman", 15, "bold"),
                          highlightbackground="blue",
                          fg="white", width="18",command=self.graph)
        grpbtn.grid(row=2, column=0)

        grp2btn = Button(buttonframe, text="Generate Graph", font=("times new roman", 15, "bold"),
                        highlightbackground="blue",
                        fg="white", width="19", command=self.graph2)
        grp2btn.grid(row=2, column=1)


        mailframe = Frame(self.root,bd=0, relief=RIDGE, bg="#E0FFFF")
        mailframe.place(x=700, y=80, width=600, height=300)

        img2 = Image.open("images/mail.png")
        img2 = img2.resize((75, 75), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(img2)

        r_lbl = Label(mailframe, image=self.image2)
        r_lbl.place(x=0, y=0, width=60, height=60)

        title = Label(mailframe, bd=0, relief=RIDGE, text="EMAIL PANEL", font=("Phosphate", 30, "bold"),bg="#E0FFFF"
                                )
        title.place(x=60, y=0)


        img3 = Image.open("images/settings.png")
        img3 = img3.resize((75, 75), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(img3)

        r_lbl1 = Button(mailframe, image=self.image3,command=self.setting_window)
        r_lbl1.place(x=540, y=0, width=60, height=60)

        self.varch=StringVar()
        single=Radiobutton(mailframe,value="single",command=self.check_sorb,variable=self.varch,text="Single",font=("times new roman",25,"bold"),bg="#E0FFFF").place(x=10,y=80)
        bulk = Radiobutton(mailframe,value="bulk",command=self.check_sorb, variable=self.varch,text="Bulk", font=("times new roman", 25, "bold"), bg="#E0FFFF").place(x=130,
                                                                                                                 y=80)
        self.varch.set("single")
        to = Label(mailframe,text="To {Email Address}",font=("times new roman", 15, "bold"),bg="#E0FFFF").place(x=0,y=110)
        sub = Label(mailframe, text="Subject", font=("times new roman", 15, "bold"), bg="#E0FFFF").place(x=0,
                                                                                                                   y=150)

        msg = Label(mailframe, text="Message", font=("times new roman", 15, "bold"), bg="#E0FFFF").place(x=0,
                                                                                                                   y=190)
        self.txtto= Entry(mailframe,font=("times new roman", 15, "bold"),bg="Light Yellow")
        self.txtto.place(x=140,y=110,width=190)

        self.txtsub = Entry(mailframe, font=("times new roman", 15, "bold"), bg="Light Yellow")
        self.txtsub.place(x=140, y=150, width=250)

        self.txtmsg = Text(mailframe, font=("times new roman", 12, "bold"), bg="Light Yellow")
        self.txtmsg.place(x=140, y=190, width=250,height=60)
        self.brbtn = Button(mailframe,command=self.browsefile, text="BROWSE", font=("times new roman", 15, "bold"),
                         highlightbackground="red",
                         fg="white", width="15",state=DISABLED)
        self.brbtn.place(x=350, y=113)

        sendbtn = Button(mailframe,command=self.send_email, text="SEND", font=("times new roman", 15, "bold"),
                           highlightbackground="green",
                           fg="white", width="15")
        sendbtn.place(x=450,y=145)

        clrbtn = Button(mailframe,command=self.clear1, text="CLEAR", font=("times new roman", 15, "bold"),
                          highlightbackground="black",
                          fg="white", width="15")
        clrbtn.place(x=450, y=175)

        self.allemails = Label(mailframe,  font=("times new roman", 15, "bold"), bg="#E0FFFF",fg="Blue")
        self.allemails.place(x=40,  y=260)


        self.sentem = Label(mailframe,  font=("times new roman", 15, "bold"), bg="#E0FFFF",fg="Green")
        self.sentem.place(x=110, y=260)

        self.spamem = Label(mailframe,  font=("times new roman", 15, "bold"), bg="#E0FFFF",fg="Red")
        self.spamem.place(x=180, y=260)

        self.leftem = Label(mailframe,  font=("times new roman", 15, "bold"), bg="#E0FFFF",fg="Black")
        self.leftem.place(x=250, y=260)



        # right label frame


        # table frame
        tableframe = Frame(root, bd=0, bg="white", relief=RIDGE)
        tableframe.place(x=103, y=360, width=1200, height=360)

        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)
        self.attendancetable = ttk.Treeview(tableframe, column=("Student ID","Name","Department","Email","Time","Date","Attendance Status"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendancetable.xview)
        scroll_y.config(command=self.attendancetable.yview)
        self.attendancetable.heading("Student ID", text="Student ID")

        self.attendancetable.heading("Name", text="Name")
        self.attendancetable.heading("Department", text="Department")
        self.attendancetable.heading("Email", text="Email")
        self.attendancetable.heading("Date", text="Date")
        self.attendancetable.heading("Time", text="Time")

        self.attendancetable.heading("Attendance Status", text="Attendance Status")
        self.attendancetable["show"] = "headings"
        self.attendancetable.pack(fill=BOTH, expand=1)

        self.attendancetable.bind("<ButtonRelease>", self.getcursor)

        self.chcfileexist()

    def update_data(self):
        if self.id_entry.get()=="" or self.dep_entry.get()=="" or self.date_entry.get()=="" or self.name_entry.get()=="" or self.time_entry.get()=="" or self.email_entry.get()=="" or self.attendance_combo=="Status":
            messagebox.showerror("Error","All Fields are Necessary",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do You Want To Update Student Details",parent=self.root)
                if Upadate>0:

                    self.email_entry.get(),
                    self.dep_entry.get(),
                    self.time_entry.get(),
                    self.date_entry.get(),
                    self.name_entry.get(),
                    self.id_entry.get(),
                    self.attendance_combo.get()
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student details are Updated", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    def reset_data(self):
        self.var_dep.set("")
        self.var_date.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_time.set("")
        self.var_attid.set("")
        self.status.set("Status")


    def fetchdata(self,rows):
        self.attendancetable.delete(*self.attendancetable.get_children())
        for i in rows:
            self.attendancetable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(filename) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to Export",parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                              filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Data has been Exported"+os.path.basename(filename)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def getcursor(self,event=""):
        cursorrow=self.attendancetable.focus()
        content=self.attendancetable.item(cursorrow)
        rows=content['values']
        self.var_attid.set(rows[0]),
        self.var_name.set(rows[1]),

        self.var_dep.set(rows[2]),
        self.var_email.set(rows[3]),
        self.var_time.set(rows[4]),

        self.var_date.set(rows[5]),
        self.status.set(rows[6])


    def browsefile(self):
        global data
        op= filedialog.askopenfile(initialdir='/',title="Select Excel file",filetypes=(("All files",".csv"),("Excel files",".xls")))
        if op != None:
            data = pd.read_csv(op.name)
            self.txtto.insert(0,str(op.name.split("/")[-1]))

            if 'Email' in data.columns:
                self.emails = list(data['Email'])
                c = []

                for i in self.emails:

                    if pd.isnull(i) == False:
                        c.append(i)

                self.emails = c
                if len(self.emails)>0:
                    self.txtto.config(state=NORMAL)
                    self.txtto.delete(0,END)
                    self.txtto.insert(0,str(op.name.split("/")[-1]))
                    self.txtto.config(state='readonly')
                    self.allemails.config(text="Total:  "+str(len(self.emails)))
                    self.sentem.config(text="Sent:  " + str(len(self.emails)))
                    self.leftem.config(text="Left:  " + str(len(self.emails)))
                    self.spamem.config(text="Spam:  " + str(len(self.emails)))

                else:
                    messagebox.showerror("Error","This file does not have any emails",parent=self.root)
            else:
                messagebox.showerror("Error","Please select file which has an Email Column",parent=self.root)

    def send_email(self):
        x=len(self.txtmsg.get('1.0',END))
        if self.txtto.get()=="" or self.txtsub.get()=="" or x==1:
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            if self.varch.get()=="single":
                status=mailfunction.email_send_function(self.txtto.get(),self.txtsub.get(),self.txtmsg.get('1.0',END),self.from_,self.pass_)
                if status=="s":
                    messagebox.showinfo("Success", "Email has been sent", parent=self.root)
                if status=="f":
                    messagebox.showerror("Error", "Email has not been sent", parent=self.root)

            if self.varch.get()=="bulk":
                self.failed=[]
                self.s_count=0
                self.f_count=0
                for x in self.emails:
                    status=mailfunction.email_send_function(x, self.txtsub.get(), self.txtmsg.get('1.0', END),
                                                     self.from_, self.pass_)
                    if status == "s":
                        self.s_count+=1
                    if status == "f":
                        self.f_count+=1
                    self.status_bar()


                messagebox.showinfo("Success", "Email has been sent,Please Check Status", parent=self.root)




    def status_bar(self):
        self.allemails.config(text="Status:  " + str(len(self.emails))+"=>>")
        self.sentem.config(text="Sent:  " + str(self.s_count))
        self.leftem.config(text="Left:  " + str(len(self.emails)-(self.s_count+self.f_count)))
        self.spamem.config(text="Spam:  " + str(self.f_count))
        self.allemails.update()
        self.sentem.update()
        self.leftem.update()
        self.spamem.update()

    def graph(self):



        data = pd.read_csv(r'/Users/kaivanvisaria/PycharmProjects/miniproj/login_database/Attendance.csv')
        df = data.groupby(['Department','Status'])['Name'].count().unstack('Status')
        df.plot.bar()
        plt.show()

    def graph2(self):



        data2 = pd.read_csv(r'/Users/kaivanvisaria/PycharmProjects/miniproj/login_database/Attendance.csv')
        df2 = data2.groupby(['Status','Date'])['Name'].count().unstack('Status')
        df2.plot.bar()
        plt.show()







    def check_sorb(self):
        if self.varch.get()=="single":
            messagebox.showinfo("Success", "Single", parent=self.root)
            self.brbtn.config(state=DISABLED)
            self.txtto.config(state=NORMAL)
            self.txtto.delete(0,END)



        else :
            messagebox.showinfo("Success", "Bulk", parent=self.root)
            self.brbtn.config(state=NORMAL)
            self.txtto.delete(0, END)
            self.txtto.config(state='readonly')


    def clear1(self):
        self.txtto.delete(0,END)
        self.txtsub.delete(0, END)
        self.txtmsg.delete('1.0', END)
        self.varch.set('single')
        self.brbtn.config(state=DISABLED)
        self.leftem.config(text="")
        self.spamem.config(text="")
        self.sentem.config(text="")
        self.allemails.config(text="")







    def setting_window(self):
        self.chcfileexist()
        self.root2=Toplevel()
        self.root2.title("Setting")
        self.root2.geometry("700x450+350+0")
        self.root2.focus_force()
        self.root2.grab_set()
        title2 = Label(self.root2, bd=0, relief=RIDGE, text="Credentials Settings",image=self.image3, font=("Phosphate", 30, "bold"), bg="red",fg="white",padx=10,compound=LEFT,anchor="w"
                      ).place(x=0,y=0,relwidth=1)
        desc2=Label(self.root2,text="Enter the EMAIL address and password of your google account",font=("times new roman", 15, "bold"),bg="yellow",fg="black").place(x=0,y=80,relwidth=1)

        em = Label(self.root2, text="Email Address", font=("times new roman", 15, "bold"), bg="white").place(x=0,
                                                                                                                   y=110)
        pas = Label(self.root2, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=0,
                                                                                                         y=150)


        self.txtem = Entry(self.root2,font=("times new roman", 15, "bold"),bg="Light Yellow")
        self.txtem.place(x=140,y=110,width=250)

        self.txtpas = Entry(self.root2, font=("times new roman", 15, "bold"), bg="Light Yellow")
        self.txtpas.place(x=140, y=150, width=250)

        savebtn = Button(self.root2,command=self.save_settings, text="SAVE", font=("times new roman", 15, "bold"),
                         highlightbackground="blue",
                         fg="white", width="15")
        savebtn.place(x=0, y=245)

        clrbtn2 = Button(self.root2,command=self.clear2, text="CLEAR", font=("times new roman", 15, "bold"),
                        highlightbackground="black",
                        fg="white", width="15")
        clrbtn2.place(x=150, y=245)
        self.txtem.insert(0,self.from_)
        self.txtpas.insert(0,self.pass_)


    def clear2(self):
        self.txtpas.delete(0,END)
        self.txtem.delete(0,END)


    def chcfileexist(self):
        if os.path.exists("importantemail.txt")==False:
            f = open('importantemail.txt', 'w')
            f.write(",")
            f.close()
        f2=open('importantemail.txt','r')
        self.credentials=[]
        for i in f2:
            self.credentials.append([i.split(",")[0],i.split(",")[1]])
        self.from_=self.credentials[0][0]
        self.pass_=self.credentials[0][1]





    def save_settings(self):
        if self.txtem.get()=="" or self.txtpas.get()=="":
            messagebox.showerror("Error","All fields are necessary",parent=self.root2)
        else:
            f=open('importantemail.txt','w')
            f.write(self.txtem.get()+","+self.txtpas.get())
            f.close()
            messagebox.showinfo("Succcess","Saved",parent=self.root2)
            self.chcfileexist()

root=Tk()
obj=Attendance(root)
root.mainloop()
