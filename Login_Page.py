
import tkinter
from tkinter import *
import Register
import Control_dynamic_auto_update
import forget
from tkinter import messagebox
import urllib3
import json

def log():
    http = urllib3.PoolManager()
    def login():
        r=http.request('GET',"https://deepakkumarpandeychs.000webhostapp.com/getstatus2.php")
        data = r.data.decode('utf-8')
        data=data[2:-2].split("},{")
        l=list()
        for i in data:
            l.append(i.split(","))
        data=[]
        for i in l:
            p=[i[0][8:-1],i[1][12:-1]]
            data.append(p)
            p=[]
        x=e1.get()
        y=e2.get()
        l=0

        for i in data:

            l+=1
            if x==i[0] and y==i[1]:

                messagebox.showinfo(title="Welcome", message="Hi! Welcome to Home control")
                log.destroy()
                Control_dynamic_auto_update.control()
                
                break

            if l==len(data):

                messagebox.showinfo(title="ERROR", message="User name or Password incorrect")

    def reg():
        log.destroy()
        Register.page()
        

    def forg():
            log.destroy()
            forget.forget()
        
    log=tkinter.Tk()
    log.title("Home Login")
    log.geometry("1366x768")
    log["bg"]="black"
    log["bd"]="150"

    f1=Frame(log,bg="black",height="500",width="900")
    f1.pack(side="top")

    l1=Label(f1,text=("Login Page"),font=("arial",50),bg="black",fg="white")
    l1.place(x=300,y=130)
    l2=Label(f1,text=("User Name"),font=("arial",25),bg="black",fg="white")
    l2.place(x=270,y=230)
    l3=Label(f1,text=("Password"),font=("arial",25),bg="black",fg="white")
    l3.place(x=270,y=280)

    e1=Entry(f1,bg="white",width=15,font=("arial",15),bd=2)
    e1.place(x=500,y=240)
    e2=Entry(f1,bg="white",width=15,font=("arial",15),bd=2,show="*")
    e2.place(x=500,y=290)

    b1=Button(f1,text="     Login     ",font="10",bg="white",fg="black",command=login)
    b1.place(x=420,y=350)
    b2=Button(f1,text="        Register      ",font="10",bg="white",fg="black",command=reg)
    b2.place(x=300,y=400)
    b3=Button(f1,text="Forget password",font="10",bg="white",fg="black",command=forg)
    b3.place(x=490, y=400)

    log.mainloop()

log()
