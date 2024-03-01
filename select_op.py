from tkinter import *
from PIL import Image,ImageTk
class Select:
    def __init__(self,root):
        self.root=root
        self.root.title("Dashboard")
        self.root.geometry("1920x1080+0+0")
        self.bg=ImageTk.PhotoImage(file="register/images/back.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        frame1=Frame(self.root,bg="light sky blue")
        frame1.place(x=500,y=250,width=550,height=300)
        title=Label(frame1,text="Choose Option: ",font=("times new roman",20,"bold"),bg="sky blue",fg="red").place(x=50,y=20)
        self.btn_img=ImageTk.PhotoImage(file="upload.png")
        logout_btn = Button(frame1, cursor="hand2",command=self.login_window,text="Log out", bg="sky blue", fg="red", bd=0,font=("times new roman" ,15,"bold","underline")).place(x=430, y=20)
        ibtn=Button(frame1,cursor="hand2",command=self.image_op,image=self.btn_img).place(x=50,y=60)
        self.btn_cam=ImageTk.PhotoImage(file="camera.png")
        cbtn=Button(frame1,cursor="hand2",command=self.cam_op,image=self.btn_cam).place(x=300,y=60)
    def login_window(self):
        self.root.destroy()
        import login
    def image_op(self):
        import i_object_detection
    def cam_op(self):
        import  Object_Detection
root=Tk()
obj=Select(root)
root.mainloop()
