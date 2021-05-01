from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import pymysql
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Welcome to Student Details")


        #variables
        self.var_id = StringVar()
        self.var_dep = StringVar()
        self.var_sem = StringVar()
        self.var_year = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_gender = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_div = StringVar()
        self.var_prof = StringVar()
        self.var_lec = StringVar()
        self.var_sub = StringVar()

        self.var_searchby=StringVar()
        self.var_sbans=StringVar()







        images = Image.open("images/smd.png")
        images = images.resize((1500, 900), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(images)
        bg11 = Label(self.root, image=self.bg11).place(x=0, y=0, relwidth=1, relheight=1)



        #main_frame=Frame(bg11,bd=2,bg="#fff8f2")
        #main_frame.place(x=0,y=25,width=1500,height=600)

        #left label frame
        

        left_frame=LabelFrame(root,bd=0,relief=RIDGE,text="STUDENT DETAILS",font=("Phosphate",25,"bold"),bg="white")
        left_frame.place(x=40,y=30,width=700,height=580)



        img1 = Image.open("images/studentgirl.png")
        img1 = img1.resize((200, 200), Image.ANTIALIAS)
        self.leftimage = ImageTk.PhotoImage(img1)

        f_lbl=Label(left_frame,image=self.leftimage)
        f_lbl.place(x=2,y=0,width=200,height=300)

        #current course
        currentcourse_frame=LabelFrame(left_frame,bd=0,bg="white",relief=RIDGE,text="Current Course Information",font=("Times New Roman",15,"bold"))
        currentcourse_frame.place(x=0, y=255, width=680, height=120)

        #department
        dep_lable=Label(currentcourse_frame,text="Department",font=("times new roman",15,"bold"))
        dep_lable.grid(row=0,column=0,padx=10,sticky=W)
        self.dep_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),width=25)
        self.dep_combo["values"]=("Select Your Department","Computer Science","IT","EXTC","ETRX","Mechanical Engineering")
        self.dep_combo.current(0)

        self.dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Semester
        course_label=Label(currentcourse_frame,text="Semester",font=("times new roman",15,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        self.course_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_sem,font=("times new roman",15,"bold"),width=25)
        self.course_combo["values"]=("Select Your Semester","Semester-1","Semester-2")
        self.course_combo.current(0)
        self.course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label = Label(currentcourse_frame, text="Year", font=("times new roman", 15, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        self.year_combo = ttk.Combobox(currentcourse_frame,textvariable=self.var_year, font=("times new roman", 15, "bold"), width=25)
        self.year_combo["values"] = ("Select Year", "FY", "SY", "TY", "LY")
        self.year_combo.current(0)
        self.year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Class Student course
        studentclass_frame = LabelFrame(left_frame, bd=0, bg="white", relief=RIDGE, text="Personal Details",
                                         font=("times new roman", 15, "bold"))
        studentclass_frame.place(x=200, y=0, width=480, height=260)

        rollno_label = Label(studentclass_frame, text="Roll Number", font=("times new roman", 15, "bold"))
        rollno_label.grid(row=0, column=0, padx=10, sticky=W)
        self.rollno_entry=ttk.Entry(studentclass_frame,textvariable=self.var_roll,width=7,font=("times new roman", 15, "bold"))
        self.rollno_entry.grid(row=0,column=1,padx=10,pady=5 ,sticky=W)

        name_label = Label(studentclass_frame, text="Full Name", font=("times new roman", 15, "bold"))
        name_label.grid(row=0, column=2, padx=10,pady=5 ,sticky=W)
        self.name_entry = ttk.Entry(studentclass_frame,textvariable=self.var_name, width=7, font=("times new roman", 15, "bold"))
        self.name_entry.grid(row=0, column=3,padx=10,pady=5 ,sticky=W)

        div_label = Label(studentclass_frame, text="Division", font=("times new roman", 15, "bold"))
        div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.div_entry = ttk.Entry(studentclass_frame,width=7,textvariable=self.var_div, font=("times new roman", 15, "bold"))
        self.div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        gender_label = Label(studentclass_frame, text="Gender", font=("times new roman", 15, "bold"))
        gender_label.grid(row=1, column=2, padx=10, sticky=W)
        self.gender_combo = ttk.Combobox(studentclass_frame,textvariable=self.var_gender, font=("times new roman", 15, "bold"), width=15)
        self.gender_combo["values"] = ("Select Gender","Male","Female")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        email_label = Label(studentclass_frame, text="Email ID", font=("times new roman", 15, "bold"))
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.email_entry = ttk.Entry(studentclass_frame,textvariable=self.var_email, width=20, font=("times new roman", 15, "bold"))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W,columnspan=2)

        phone_label = Label(studentclass_frame, text="Phone Number", font=("times new roman", 15, "bold"))
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W,columnspan=2)
        self.phone_entry = ttk.Entry(studentclass_frame,textvariable=self.var_phone, width=10, font=("times new roman", 15, "bold"))
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W,columnspan=3)

        dob_label = Label(studentclass_frame, text="Date of Birth", font=("times new roman", 15, "bold"))
        dob_label.grid(row=3, column=2, padx=10, pady=5, sticky=W, columnspan=2)
        self.dob_entry = ttk.Entry(studentclass_frame,textvariable=self.var_dob, width=8, font=("times new roman", 15, "bold"))
        self.dob_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W, columnspan=3)

        address_label = Label(studentclass_frame, text="Address", font=("times new roman", 15, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W,columnspan=2)
        self.address_entry = ttk.Entry(studentclass_frame,textvariable=self.var_address, width=30, font=("times new roman", 15, "bold"))
        self.address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W,columnspan=4)


        ID_label = Label(studentclass_frame, text="Student ID", font=("times new roman", 15, "bold"))
        ID_label.grid(row=5, column=0, padx=10, pady=5, sticky=W,columnspan=2)
        self.id_entry = ttk.Entry(studentclass_frame,textvariable=self.var_id, width=10, font=("times new roman", 15, "bold"))
        self.id_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W,columnspan=4,rowspan=2)


        # current course
        currentprofessor_frame = LabelFrame(left_frame, bd=0, bg="white", relief=RIDGE, text="Lecture Details",
                                         font=("times new roman", 15, "bold"))
        currentprofessor_frame.place(x=0, y=375, width=680, height=130)

        subjectname_label = Label(currentprofessor_frame, text="Subject Name", font=("times new roman", 15, "bold"))
        subjectname_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.subjectname_entry = ttk.Entry(currentprofessor_frame,textvariable=self.var_sub,width=10, font=("times new roman", 15, "bold"))
        self.subjectname_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        professorname_label = Label(currentprofessor_frame, text="Professor Name", font=("times new roman", 15, "bold"))
        professorname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        self.professorname_entry = ttk.Entry(currentprofessor_frame,textvariable=self.var_prof, width=20, font=("times new roman", 15, "bold"))
        self.professorname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        lectim_lable = Label(currentprofessor_frame, text="Lecture Time", font=("times new roman", 15, "bold"))
        lectim_lable.grid(row=1, column=0, padx=10, sticky=W)
        self.lectim_combo = ttk.Combobox(currentprofessor_frame,textvariable=self.var_lec, font=("times new roman", 15, "bold"), width=20)
        self.lectim_combo["values"] = (
        "Select Lecture Timings", "9:30-10:30","10:30-12:30","10:30-11:30", "11:30-12:30", "1:15-3:15", "3:15-5:15","1:15-2:15","2:15-3:15","3:15-5:15","3:15-4:15","4:15-5:15")
        self.lectim_combo.current(0)

        self.lectim_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(currentprofessor_frame,variable=self.var_radio1,text="Take Sample Photo",value="Yes")
        radiobtn1.grid(row=2,column=0)


        radiobtn2 = ttk.Radiobutton(currentprofessor_frame,variable=self.var_radio1, text="No Sample Photo", value="No")
        radiobtn2.grid(row=2, column=1)

        btn_frame=Frame(left_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=505,width=680,height=50)

        savebtn=Button(btn_frame,text="SAVE",command=self.add_data,font=("times new roman", 15, "bold"),highlightbackground="blue",fg="white",width="15")
        savebtn.grid(row=0,column=0)

        updatebtn = Button(btn_frame, text="UPDATE",command=self.update_data, font=("times new roman", 15, "bold"), highlightbackground="green",
                         bg="green",fg="white", width="15")
        updatebtn.grid(row=0, column=1)

        deletebtn = Button(btn_frame, text="DELETE",command=self.delete_data, font=("times new roman", 15, "bold"), highlightbackground="red",
                           fg="white", width="15")
        deletebtn.grid(row=0, column=2)

        resetbtn = Button(btn_frame, text="RESET",command=self.reset_data, font=("times new roman", 15, "bold"), highlightbackground="orange",
                           fg="white", width="15")
        resetbtn.grid(row=0, column=3)

        takephotobtn = Button(btn_frame,command=self.generate_dataset,text="CAPTURE YOURSELF", font=("times new roman", 15, "bold"), highlightbackground="purple",
                           fg="white", width="30")
        takephotobtn.place(x=0,y=20)

        updatephotobtn = Button(btn_frame, text="UPDATE PHOTO SAMPLE",command=self.generate_dataset, font=("times new roman", 15, "bold"), highlightbackground="purple",
                          fg="white", width="30")
        updatephotobtn.place(x=250,y=20)

        # right label frame
        right_frame = LabelFrame(root, bd=0, relief=RIDGE, text="Student Dashboard",
                                font=("Phosphate", 25, "bold"), bg="white")
        right_frame.place(x=720, y=30, width=680, height=580)

        img2 = Image.open("images/BOOKS.png")
        img2 = img2.resize((150, 150), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(img2)

        r_lbl = Label(right_frame, image=self.image2)
        r_lbl.place(x=0, y=0, width=150, height=150)

        img3 = Image.open("images/grad.png")
        img3 = img3.resize((150, 150), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(img3)

        r1_lbl = Label(right_frame, image=self.image3)
        r1_lbl.place(x=150, y=0, width=150, height=150)

        img4 = Image.open("images/BRAIN.png")
        img4 = img4.resize((170, 170), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(img4)

        r2_lbl = Label(right_frame, image=self.image4)
        r2_lbl.place(x=300, y=0, width=150, height=130)

        img5 = Image.open("images/test.png")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(img5)

        r3_lbl = Label(right_frame, image=self.image5)
        r3_lbl.place(x=470, y=0, width=150, height=150)



        #table frame
        tableframe= Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        tableframe.place(x=0,y=215,width=670,height=300)

        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)
        self.studenttable=ttk.Treeview(tableframe,column=("Student ID","Department","Semester","Year","Roll Number","Name","Division","Gender","Email","Phone Number","Date of Birth","Address","Subject Name","Professor Name","Lecture Timings","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studenttable.xview)
        scroll_y.config(command=self.studenttable.yview)

        self.studenttable.heading("Student ID",text="Student ID")
        self.studenttable.heading("Department",text="Department")
        self.studenttable.heading("Semester", text="Semester")
        self.studenttable.heading("Year", text="Year")
        self.studenttable.heading("Roll Number", text="Roll Number")
        self.studenttable.heading("Name", text="Name")
        self.studenttable.heading("Division", text="Division")
        self.studenttable.heading("Gender", text="Gender")
        self.studenttable.heading("Email", text="Email")
        self.studenttable.heading("Phone Number", text="Phone Number")
        self.studenttable.heading("Date of Birth", text="Date of Birth")
        self.studenttable.heading("Address", text="Address")
        self.studenttable.heading("Subject Name", text="Subject Name")
        self.studenttable.heading("Professor Name", text="Professor Name")
        self.studenttable.heading("Lecture Timings", text="Lecture Timings")
        self.studenttable.heading("Photo", text="Photo")
        self.studenttable["show"]="headings"
        self.studenttable.pack(fill=BOTH,expand=1)
        self.studenttable.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

        # search system
        search_frame = LabelFrame(right_frame, bd=0, bg="white", relief=RIDGE, text="Search",
                                  font=("times new roman", 15, "bold"))
        search_frame.place(x=5, y=150, width=670, height=70)

        search_label = Label(search_frame, text="Search By", font=("times new roman", 15, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(search_frame, font=("times new roman", 15, "bold"), width=13,
                                         textvariable=self.var_searchby)
        self.search_combo["values"] = (
            "Select", "Roll Number", "Name")
        self.search_combo.current(0)

        self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.search_entry = ttk.Entry(search_frame, width=14, font=("times new roman", 15, "bold"),
                                      textvariable=self.var_sbans)
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        srchbtn = Button(search_frame, text="Search", command=self.search_data, font=("times new roman", 15, "bold"),
                         highlightbackground="white",
                         fg="black", width="15")
        srchbtn.grid(row=0, column=3)

        showbtn = Button(search_frame, text="Show All Records", command=self.fetch_data,
                         font=("times new roman", 15, "bold"), highlightbackground="white",
                         fg="black", width="15")
        showbtn.grid(row=0, column=4)

        #function

    def add_data(self):
        if self.dep_combo.get()=="Select Your Department" or self.course_combo.get()=="Select Your Semester" or self.year_combo.get()=="Select Year" or self.rollno_entry.get()=="" or self.name_entry.get()=="" or self.div_entry.get()=="" or self.gender_combo.get()=="Select Gender" or self.email_entry.get()=="" or self.phone_entry.get()=="" or self.dob_entry.get()=="" or self.professorname_entry.get()=="" or self.subjectname_entry.get()=="" or self.lectim_combo.get()=="Select Lecture Timings" or self.id_entry.get()=="":
            messagebox.showerror("Error","All Fields are Necessary",parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                               database="face-recognition")
                cur = conn.cursor()

                cur.execute(
                    "INSERT INTO `face-recognition`.`student` (`ID`,`department`, `semester`, `year`, `roll number`, `name`, `division`, `gender`, `email`, `phone`, `DOB`, `address`, `professor name`, `subject name`, `lecture timings`,`photosample`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            ( self.id_entry.get(),self.dep_combo.get(), self.course_combo.get(), self.year_combo.get(), self.rollno_entry.get(),
                    self.name_entry.get(), self.div_entry.get(), self.gender_combo.get(), self.email_entry.get(),
                    self.phone_entry.get(), self.dob_entry.get(), self.address_entry.get(), self.professorname_entry.get(),
                    self.subjectname_entry.get(), self.lectim_combo.get(), self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details are Recorded successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                #fetch data
    def fetch_data(self):
        conn=pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                               database="face-recognition")
        cur = conn.cursor()
        cur.execute("Select * from student")
        data=cur.fetchall()

        if len(data)!=0:
            self.studenttable.delete(*self.studenttable.get_children())
            for i in data:
                self.studenttable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                               database="face-recognition")
        cur = conn.cursor()

        if self.search_combo.get()=="Roll Number":
            sql1 ="SELECT * FROM `face-recognition`.`student` WHERE (`roll number` = %s)"
            val1 = (self.var_sbans.get(),)
            cur.execute(sql1, val1)
            data1=cur.fetchall()
            if len(data1)!=0:
                self.studenttable.delete(*self.studenttable.get_children())
                for i in data1:
                    self.studenttable.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showerror("Error","No Student record with this roll number",parent=self.root)
        elif self.search_combo.get()=="Name":
            sql = "SELECT * FROM `face-recognition`.`student` WHERE (`name` = %s)"
            val = (self.var_sbans.get(),)
            cur.execute(sql, val)
            data1 = cur.fetchall()
            if len(data1) != 0:
                self.studenttable.delete(*self.studenttable.get_children())
                for i in data1:
                    self.studenttable.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showerror("Error", "No Student record with this name", parent=self.root)
        conn.close()






        #GET CURSOR

    def get_cursor(self,event=""):
        cur_focus=self.studenttable.focus()
        content=self.studenttable.item(cur_focus)
        data=content["values"]


        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_year.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_address.set(data[11]),
        self.var_prof.set(data[13]),
        self.var_sub.set(data[12]),
        self.var_lec.set(data[14]),
        self.var_radio1.set(data[15])

    #update function

    def update_data(self):
        if self.dep_combo.get()=="Select Your Department" or self.course_combo.get()=="Select Your Semester" or self.year_combo.get()=="Select Year" or self.rollno_entry.get()=="" or self.name_entry.get()=="" or self.div_entry.get()=="" or self.gender_combo.get()=="Select Gender" or self.email_entry.get()=="" or self.phone_entry.get()=="" or self.dob_entry.get()=="" or self.professorname_entry.get()=="" or self.subjectname_entry.get()=="" or self.lectim_combo.get()=="Select Lecture Timings" or self.id_entry.get()=="":
            messagebox.showerror("Error","All Fields are Necessary",parent=self.root)

        else:
            try:
                Upadate=messagebox.askyesno("Update","Do You Want To Update Student Details",parent=self.root)
                if Upadate>0:

                    conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                   database="face-recognition")
                    cur = conn.cursor()
                    cur.execute("UPDATE `face-recognition`.`student` SET `ID` = %s,`department` = %s, `semester` = %s, `year` = %s, `name` = %s, `division` = %s, `gender` = %s, `email` = %s, `phone` = %s, `DOB` = %s, `address` = %s, `professor name` = %s, `subject name` = %s, `lecture timings` = %s ,`photosample`=%s WHERE `roll number`= %s",(
                        self.id_entry.get(),
                        self.dep_combo.get(),
                        self.course_combo.get(),
                        self.year_combo.get(),

                        self.name_entry.get(),
                        self.div_entry.get(),
                        self.gender_combo.get(),
                        self.email_entry.get(),
                        self.phone_entry.get(),
                        self.dob_entry.get(),
                        self.address_entry.get(),
                        self.professorname_entry.get(),
                        self.subjectname_entry.get(),
                        self.lectim_combo.get(),
                        self.var_radio1.get(),
                        self.rollno_entry.get()
                        ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details are Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete
    def  delete_data(self):
        if self.rollno_entry.get()=="":
            messagebox.showerror("Error","Student Roll Number Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do You Want to Delete the Student record",parent=self.root)
                if delete>0:

                    conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                   database="face-recognition")
                    cur = conn.cursor()
                    sql="DELETE FROM `face-recognition`.`student` WHERE (`roll number` = %s)"
                    val=(self.var_roll.get(),)
                    cur.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Record",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Your Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Your Semester")
        self.var_roll.set("")
        self.var_sub.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gender.set("Select Gender")
        self.var_div.set("")
        self.var_prof.set("")
        self.var_lec.set("Select Lecture Timings")
        self.var_radio1.set("")
        self.var_sub.set("")
        self.var_name.set("")
        self.var_id.set("")

        #generate data set take photo sample
    def generate_dataset(self):
        if self.dep_combo.get()=="Select Your Department" or self.course_combo.get()=="Select Your Semester" or self.year_combo.get()=="Select Year" or self.rollno_entry.get()=="" or self.name_entry.get()=="" or self.div_entry.get()=="" or self.gender_combo.get()=="Select Gender" or self.email_entry.get()=="" or self.phone_entry.get()=="" or self.dob_entry.get()=="" or self.professorname_entry.get()=="" or self.subjectname_entry.get()=="" or self.lectim_combo.get()=="Select Lecture Timings":
            messagebox.showerror("Error","All Fields are Necessary",parent=self.root)

        else:
            try:


                    conn = pymysql.connect(host="localhost", user="root", password="Jadhavji09",
                                   database="face-recognition")
                    cur = conn.cursor()
                    cur.execute("select * from student")
                    myresults=cur.fetchall()
                    id=0
                    for x in myresults:
                        id+=1
                    cur.execute(
                         "UPDATE `face-recognition`.`student` SET `department` = %s,`roll number`=%s, `semester` = %s, `year` = %s, `name` = %s, `division` = %s, `gender` = %s, `email` = %s, `phone` = %s, `DOB` = %s, `address` = %s, `professor name` = %s, `subject name` = %s, `lecture timings` = %s ,`photosample`=%s WHERE `ID`= %s",
                          (
                    self.dep_combo.get(),
                    self.course_combo.get(),
                    self.year_combo.get(),
                    self.rollno_entry.get(),

                    self.name_entry.get(),
                    self.div_entry.get(),
                    self.gender_combo.get(),
                    self.email_entry.get(),
                    self.phone_entry.get(),
                    self.dob_entry.get(),
                    self.address_entry.get(),
                    self.professorname_entry.get(),
                    self.subjectname_entry.get(),
                    self.lectim_combo.get(),
                    self.var_radio1.get(),
                    self.var_id.get()==id+1


                ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor
                        #mini neighbour
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(myframe),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_RGB2GRAY)
                            file_name_path="DATA/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating Data Set Completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


root=Tk()
obj=Student(root)
root.mainloop()

#INSERT INTO `face-recognition`.`student` (`department`, `semester`, `year`, `roll number`, `name`, `division`, `gender`, `email`, `phone`, `DOB`, `address`, `professor name`, `subject name`, `lecture timings`) VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14');

#INSERT INTO `face-recognition`.`student` (`department`, `semester`, `year`, `roll number`, `name`, `division`, `gender`, `email`, `phone`, `DOB`, `address`, `professor name`, `subject name`, `lecture timings`) VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14');

