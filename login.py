from tkinter import *
#import pymysql
from tkinter import ttk,messagebox

import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1000x702+250+50")
        self.root.resizable(False,False)
        #Background Image
        self.bg = PhotoImage(file="login/images/login.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=275,y=180,width=450,height=350)
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#38a7fc",bg="white").place(x=110,y=30)
        desc=Label(Frame_login,text="Registered User Login",font=("Goudy old style",15,"bold"),fg="#42a7f5",bg="white").place(x=110,y=90)
        lbl_email=Label(Frame_login,text="Username",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=110,y=135)
        self.txt_email=Entry(Frame_login,font=("times new roman",12),bg="lightgray")
        self.txt_email.place(x=110,y=165,width=220,height=25)
        lbl_pass_= Label(Frame_login, text="Password", font=("Goudy old style", 12, "bold"), fg="gray",bg="white").place(x=110, y=200)
        self.txt_pass_ = Entry(Frame_login, font=("times new roman", 12), bg="lightgray")
        self.txt_pass_.place(x=110, y=225, width=220, height=25)
        forget_btn=Button(Frame_login,cursor="hand2",command=self.forget_pass_,text="Forget Password?",bg="white",fg="#38a7fc",bd=0,font=("times new roman",12)).place(x=215,y=195)
        login_btn=Button(Frame_login,cursor="hand2",command=self.login,text="Log In",fg="white",bg="#38a7fc",font=("times new roman",12)).place(x=110,y=265,width=100,height=25)
        register_btn=Button(Frame_login,cursor="hand2",command=self.register_window,text="Register",fg="white",bg="#38a7fc",font=("times new roman",12)).place(x=230,y=265,width=100,height=25)
    def register_window(self):
        self.root.destroy()
        import register
    def forget_pass_(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter Valid Email Id",parent=self.root)
        else:
            self.root2=Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("450x350+525+230")
            self.root2.config(bg="white")
            self.root2.focus_force()
            self.root2.grab_set()
            t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="#38a7fc").place(x=0,y=-125,relwidth=1,relheight=1)
            question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=125, y=75)
            self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
            self.cmb_quest['values'] = ("select", "Your Pet name", "your Birth Place", "your Best friend")
            self.cmb_quest.place(x=125, y=105, width=200)
            self.cmb_quest.current(0)
            answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=125, y=135)
            self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgrey")
            self.txt_answer.place(x=125, y=165, width=200)
            password = Label(self.root2, text="Enter Password", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=125, y=200)
            self.txt_password = Entry(self.root2, font=("times new roman", 15), bg="lightgrey")
            self.txt_password.place(x=125, y=230, width=200)
            chnpass_btn = Button(self.root2, cursor="hand2", command=self.chnpass_, text="Change Password", fg="white", bg="#38a7fc",font=("times new roman", 15)).place(x=150, y=275, width=150, height=30)
    def chnpass_(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="userdb")
        cur=con.cursor()
        cur.execute("select answer from user where email=%s and question=%s",(self.txt_email.get(),self.cmb_quest.get()))
        row=cur.fetchone()
        print(row)
        if row == self.txt_answer.get():
            messagebox.showerror("Error","Wrong Answer! please enter correct answer!",parent=self.root2)
        else:
            messagebox.showinfo("Successfull","Password Reset Successfull!",parent=self.root2)
            self.root2.destroy()
    def login(self):
        if self.txt_email.get()==""or self.txt_pass_.get()=="":
            messagebox.showerror("Error","Enter email and password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="userdb")
                cur=con.cursor()
                cur.execute("select * from user where email=%s and pass=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                else:
                    messagebox.showinfo("Logged In","Correct Email & Password : Login Successfull!",parent=self.root)
                    self.root.destroy()
                    import select_op
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to this: {str(es)}",parent=self.root)
    #def selected(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Select(self.new_window)

root = Tk()
obj = Login(root)
root.mainloop()
