from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration window")
        self.root.geometry("1500x900+0+0")

        # Add image file


        image = Image.open("images/register3.png")
        image = image.resize((1500, 900), Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(image)
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)




        frame1=Frame(self.root,bg="white")
        frame1.place(x=200,y=80,width=1500,height=600)
        title = Label(frame1,text="REGISTER HERE",font=("Gill Sans",50,"bold"),fg="#191970").place(x=50,y=30)

        frame2 = Frame(frame1, bg="#A7C7E7")
        frame2.place(x=660, y=0, width=1500, height=600)


        f_name = Label(frame1, text="FIRST NAME", font=("Arial Rpunded MT", 15, "bold"),fg="#191970").place(x=50, y=100)

        self.txt_name=Entry(frame1,font=("times new roman",15))
        self.txt_name.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="LAST NAME", font=("times new roman", 15, "bold"),fg="#191970").place(x=370, y=100)

        self.txt_lname = Entry(frame1, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)
        contact = Label(frame1, text="CONTACT NO", font=("times new roman", 15, "bold"),fg="#191970").place(x=50, y=160)

        self.txt_contact = Entry(frame1, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=190, width=250)

        email = Label(frame1, text="EMAIL", font=("times new roman", 15, "bold"),fg="#191970").place(x=370, y=160)

        self.txt_email = Entry(frame1, font=("times new roman", 15))
        self.txt_email.place(x=370, y=190, width=250)

        question = Label(frame1, text="SECURITY QUESTION", font=("times new roman", 15, "bold"),fg="#191970").place(x=50, y=230)

        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 15),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select", "Your First Friend","Your Birth Place","Your Favourite food")
        self.cmb_question.place(x=50, y=260, width=250)
        self.cmb_question.current(0)

        answer = Label(frame1, text="ANSWER", font=("times new roman", 15, "bold"),fg="#191970").place(x=370, y=230)

        self.txt_answer = Entry(frame1, font=("times new roman", 15))
        self.txt_answer.place(x=370, y=260, width=250)

        password = Label(frame1, text="PASSWORD", font=("times new roman", 15, "bold"),fg="#191970").place(x=50, y=305)

        self.txt_password = Entry(frame1, font=("times new roman", 15))
        self.txt_password.place(x=50, y=330, width=250)

        passwordagain = Label(frame1, text="CONFIRM YOUR PASSWORD", font=("times new roman", 15, "bold"),fg="#191970").place(x=370, y=305)

        self.txt_passwordagain = Entry(frame1, font=("times new roman", 15))
        self.txt_passwordagain.place(x=370, y=330, width=250)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree to the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",15)).place(x=50,y=400)

        btreg = Image.open("images/register.png")
        btreg = btreg.resize((300, 50), Image.ANTIALIAS)

        self.btn_image=ImageTk.PhotoImage(btreg)
        btn_register=Button(frame1,text="Register Now",bd=0,cursor="hand2",command=self.register_data,borderwidth=0,highlightbackground="blue",activebackground="green",width=14,height=2).place(x=50,y=450)
        btn_login = Button(frame1, text="Sign In", bd=0, cursor="hand2", command=self.login_window,
                              borderwidth=0, highlightbackground="green", activebackground="green",width=14,height=2).place(x=200, y=450)

    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_passwordagain.delete(0, END)
        self.txt_answer.delete(0,END)
        self.cmb_question.current(0)

    def login_window(self):
        self.root.destroy()
        import login


    def register_data(self):
        if self.txt_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_passwordagain.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_passwordagain.get():
            messagebox.showerror("Error","Password did not match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.root)

        else:
            try:


                con = pymysql.connect(host="localhost", user="root", password="Jadhavji09", database="face-recognition")
                cur = con.cursor()
                cur.execute("select * from admins where email=%s",self.txt_email.get())
                row = cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exists",parent=self.root)
                else:
                    cur.execute(
                        "insert into admins (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_name.get(), self.txt_lname.get(), self.txt_contact.get(), self.txt_email.get(),
                         self.cmb_question.get(), self.txt_answer.get(), self.txt_password.get()
                         ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                    self.clear()




            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
root=Tk()
obj=Register(root)
root.mainloop()
