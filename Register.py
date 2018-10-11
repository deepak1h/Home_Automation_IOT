import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
#import Login_Page



def page():


    def submit():
        user_ID=e1.get()
        password=e2.get()
        re=e3.get()
        name=e4.get()
        mobile=e5.get()
        email_ID=e6.get()

        if password==re:
            db=mc.connect(host="localhost",user="deepak",password="deepak!@#",database="deepak_home")
            cur=db.cursor()
            cmd="insert into users(user_ID,password,name,mobile,email_ID) values('"+user_ID+"','"+password+"','"+name+"','"+mobile+"','"+email_ID+"');"
            cur.execute(cmd)
            db.commit()
            cur.close()
            db.close()
            messagebox.showinfo(title="Congratulations", message="You are now registered")
        else:
            messagebox.showinfo(title="ERROR", message="Password not match")


    def login():
        messagebox.showinfo(title="Attention", message="Open Login Page")
        root.destroy()
        Login_Page.log()



    root=tkinter.Tk()
    root.title("Register")
    root.geometry("1366x768")
    root["bd"]=30
    root["bg"]="#141414"




    f1=Frame(root,height="700",width="1300",bg="#424242")
    f1.pack()




    l1=Label(f1,text="REGISTRATION PORTAL",font=("ubuntu",20),bg="#424242",fg="white")
    l1.place(x=500,y=50)
    l2=Label(f1,text="User ID*",font=("ubuntu",20),bg="#424242",fg="white")
    l2.place(x=350,y=150)
    l3=Label(f1,text="New Password*",font=("ubuntu",20),bg="#424242",fg="white")
    l3.place(x=350,y=200)
    l4=Label(f1,text="Re-Enter*",font=("ubuntu",20),bg="#424242",fg="white")
    l4.place(x=350,y=250)
    l5=Label(f1,text="Full Name*",font=("ubuntu",20),bg="#424242",fg="white")
    l5.place(x=350,y=300)
    l6=Label(f1,text="Mobile No.*",font=("ubuntu",20),bg="#424242",fg="white")
    l6.place(x=350,y=350)
    l7=Label(f1,text="Email ID",font=("ubuntu",20),bg="#424242",fg="white")
    l7.place(x=350,y=400)





    e1=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"))
    e1.place(x=600,y=150)
    e2=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"),show="*")
    e2.place(x=600,y=200)
    e3=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"),show="*")
    e3.place(x=600,y=250)
    e4=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"))
    e4.place(x=600,y=300)
    e5=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"))
    e5.place(x=600,y=350)
    e6=Entry(f1,bg="white",bd=1,width=30,font=("URW gothic L",15,"bold"))
    e6.place(x=600,y=400)


    b1=Button(f1,text="Submit",font=("ubuntu",20),command=submit)
    b1.place(x=500,y=490)
    b2=Button(f1,text=" Login ",font=("ubuntu",20),command=login)
    b2.place(x=700,y=490)








    root.mainloop()