from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

class login_system:
    def __init__(self,root):
        image = Image.open("images/phone.png")
        image = image.resize((700,700), Image.ANTIALIAS)
        self.root=root
        self.root.title("WELCOME TO THE LOGIN SYSTEM")
        self.root.geometry("1500x900+0+0")


        self.phone_image = ImageTk.PhotoImage(image)
        self.lbl_phone_image=Label(self.root,image=self.phone_image).place(x=50,y=50)

        login_frame=Frame(self.root,bd=5,relief=RIDGE,highlightcolor="#191970")
        login_frame.place(x=700,y=90,width=350,height=600)

        title=Label(login_frame,text="Log In Here", font=("Phosphate",40,"bold"),fg="#191970").place(x=0,y=30,relwidth=1)
        lbl_email = Label(login_frame,text="EMAIL ADDRESS", font=("Andalus",15),fg="black",bg="white").place(x=47,y=130)
        self.email=StringVar()
        self.password = StringVar()
        txt_email=Entry(login_frame,textvariable=self.email, font=("times new roman",15),bg="white").place(x=50,y=150,width=250)
        lbl_pass = Label(login_frame, text="PASSWORD", font=("Andalus", 15), fg="black", bg="white").place(x=47,
                                                                                                             y=230)
        txt_pass = Entry(login_frame,textvariable=self.password,show="*", font=("times new roman", 15), bg="white").place(x=50, y=250, width=250)
        btn_login=Button(login_frame,command=self.login,text="Log in", font=("Arial Rounded MT Bold",15),bg="#00759E",highlightbackground="#191970",fg="black",activeforeground="white",cursor="hand2").place(x=75,y=300,width=200,height=40)

        hr=Label(login_frame,bg="lightgrey").place(x=50,y=370,width=260,height=2)

        or_=Label(login_frame,text="OR",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=150,y=360)

        register_frame = Frame(self.root, bd=2, relief=RIDGE,bg="white")
        register_frame.place(x=738, y=500, width=280, height=60)

        lbl_reg = Label(register_frame, text="Don't have an account?", font=("times new roman", 13), bg="white").place(x=20,
                                                                                                             y=20)
        btn_signup = Button(register_frame,command=self.register_window, text="Sign Up", font=("times new roman", 13,"bold"), highlightbackground="grey",
                            fg="black", bd=0, activeforeground="#00759E", activebackground="white").place(x=148,
                                                                                                            y=5,width=100)

        btn_signup4 = Button(register_frame, command=self.openmain_pagewindow, text="Go To Home Page",
                            font=("times new roman", 13, "bold"), highlightbackground="grey",
                            fg="black", bd=0, activeforeground="#00759E", activebackground="white").place(x=148,
                                                                                                          y=30,
                                                                                                          width=130)

        image1 = Image.open("images/login1.png")
        image1 = image1.resize((650, 650), Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(image1)

        image2 = Image.open("images/login2.png")
        image2 = image2.resize((650, 650), Image.ANTIALIAS)
        self.im2 = ImageTk.PhotoImage(image2)

        image3 = Image.open("images/login3.png")
        image3 = image3.resize((500, 500), Image.ANTIALIAS)
        self.im3 = ImageTk.PhotoImage(image3)

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=280,y=150,width=240,height=500)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    def register_window(self):
        self.root.destroy()
        import register

    def openmain_pagewindow(self):
        self.root.destroy()
        import pagewindow



    def login(self):
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required.")

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Jadhavji09",database="face-recognition")
                cur=con.cursor()
                cur.execute("select * from admins where email=%s and password=%s",(self.email.get(),self.password.get()))
                row=cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Invalid Username or Password\n Try again with correct credentials")

                else:
                    messagebox.showinfo("Information",
                                        f"Welcome : {self.email.get()}\n Your Password: {self.password.get()}")




                con.close()







            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)






root=Tk()
obj=login_system(root)
root.mainloop()
