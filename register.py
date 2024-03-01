from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1920x1080+0+0")
        #bg image
        self.bg=ImageTk.PhotoImage(file="register/images/back.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        # side image
        self.left = ImageTk.PhotoImage(file="register/images/side.gif")
        left = Label(self.root, image=self.left).place(x=250, y=150, width=400, height=500)
        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=650,y=150,width=700,height=500)

        title =Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="#72ad0a").place(x=50,y=30)
        # row 1-------------------------------------------
        f_name = Label(frame1, text="First Name", font=("times new roman",15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_lname.place(x=370, y=130, width=250)
        #Row 2 ******************************
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_contact.place(x=50, y=200, width=250)
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_email.place(x=370, y=200, width=250)
       #-------------------row 3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=240)
        self.cmb_quest =ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("select","Your Pet name","your Birth Place","your Best friend")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)


        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_answer.place(x=370, y=270, width=250)


        #Row 4 ******************************
        password = Label(frame1, text="Enter Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_password.place(x=50, y=340, width=250)
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_cpassword.place(x=370, y=340, width=250)
        #check
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms and Condition",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("the new roman",12)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="register/images/re.png")
        btn_reg=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.reg_data).place(x=220,y=405)

        btn_signin=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=390,y=600,width=150)
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
    def login_window(self):
        self.root.destroy()
        import login
    def reg_data(self):
        if self.txt_fname.get()==""or self.txt_lname.get()==""or self.txt_contact.get()==""or self.txt_email.get()==""or self.cmb_quest.get()==""or self.txt_answer.get()==""or self.txt_password.get()==""or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree terms and condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="userdb")
                cur=con.cursor()
                cur.execute("select * from user where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "PIser already Exist, please log in or use another email!", parent=self.root)
                else:
                    cur.execute("insert into user(fname,lname,contact,email,question,answer,pass) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_quest.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Successful", "Registration successful!", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()