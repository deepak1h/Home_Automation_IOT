import tkinter
from tkinter import *
from tkinter import messagebox

import urllib3
import json
import random

def page():
    baseURL="https://deepakkumarpandeychs.000webhostapp.com/updatestatus2.php"
    http = urllib3.PoolManager()
    def check():
            o=e8.get()
            if OT==o:
                r=http.request('GET',"https://deepakkumarpandeychs.000webhostapp.com/updatestatus2.php?name="+name+"&user_ID="+user_ID+"&mobile="+mobile+"&email_ID="+email_ID+"&password="+password+"")
                data1 = r.data.decode('utf-8')
                r.close()
                print (data1)
                if data1=="success":
                    
                    messagebox.showinfo(title="Congratulations", message="You are now registered")
                    root.destroy()
                    import Login_Page
                    
                    
                else:
                    messagebox.showinfo(title="Error", message="Unable to register")
            else:
                messagebox.showinfo(title="ERROR", message="OTP not match")
    def otp():
        global OT
        OT=str(random.randint(1000,9999))
        r1=http.request('GET',"https://smsapi.engineeringtgr.com/send/?Mobile=7268969885&Password=7268969885&Message="+"OTP="+OT+"&To="+mobile+"&Key=deepaaPNrA6Cv10gEmMj5h4Z")
        data = r1.data.decode('utf-8')
        data="true"
        if "true" in data:
            messagebox.showinfo(title="Alert", message="OTP sent to your Mobile")
            l9 = Label(f1, text="OTP", font=("ubuntu", 20), bg="#424242", fg="white")
            l9.place(x=500, y=600)
            global e8
            e8 = Entry(f1, bg="white", bd=1, width=10, font=("URW gothic L", 15, "bold"))
            e8.place(x=620, y=600)
            b2 = Button(f1, text="Submit", font=("ubuntu", 20), command=check)
            b2.place(x=500, y=650)
            b2 = Button(f1, text="Resend", font=("ubuntu", 20), command=otp)
            b2.place(x=700, y=650)
            
        elif "finished your day quota." in data:
            messagebox.showinfo(title="Alert", message="unable to send Try again after 24 hr")
            root.destroy()
            import Login_Page
            
        else:
            messagebox.showinfo(title="Alert", message="unable to send OTP, retry")
       
        
    def submit():
        global mobile,name,user_ID,password,re,email_ID
        user_ID=e1.get()
        password=e2.get()
        re=e3.get()
        name=e4.get()
        mobile=e5.get()
        email_ID=e6.get()
        if "#" in user_ID+password+name+email_ID or "&" in user_ID+password+name+email_ID or "%" in user_ID+password+name+email_ID :
            messagebox.showinfo(title="ERROR", message="'%,#,&' used in any field")

        else:
            if password==re:
                
                r2=http.request('GET',"https://deepakkumarpandeychs.000webhostapp.com/getstatus2.php")
                data2 = r2.data.decode('utf-8')
                data2=data2[2:-2].split("},{")
                l=list()
                for i in data2:
                    l.append(i.split(","))
                data2=[]
                for i in l:
                    p=i[0][8:-1]
                    data2.append(p)
                    p=[]
                
                if user_ID in data2:
                    messagebox.showinfo(title="ERROR", message="This useID is taken")
                else:
                    otp()
            else:
                messagebox.showinfo(title="ERROR", message="Password not match")
            

    def login():
        
        messagebox.showinfo(title="Attention", message="Open Login Page")
        root.destroy()
        import Login_Page
        

    root=tkinter.Tk()
    root.title("Register")
    root.geometry("1366x768")
    root["bd"]=30
    root["bg"]="#141414"

    f1=Frame(root,height="700",width="1300",bg="#424242")
    f1.pack()

    l1=Label(f1,text="REGISTRATION PORTAL",font=("ubuntu",20),bg="#424242",fg="white")
    l1.place(x=500,y=50)
    l1=Label(f1,text="dont use '&,#,%' in any fields.",font=("ubuntu",10),bg="#424242",fg="white")
    l1.place(x=550,y=85)
    l2=Label(f1,text="User ID*",font=("ubuntu",20),bg="#424242",fg="white")
    l2.place(x=350,y=150)
    l3=Label(f1,text="New Password*",font=("ubuntu",20),bg="#424242",fg="white")
    l3.place(x=350,y=200)
    l4=Label(f1,text="Re-Enter*",font=("ubuntu",20),bg="#424242",fg="white")
    l4.place(x=350,y=250)
    l5=Label(f1,text="First Name*",font=("ubuntu",20),bg="#424242",fg="white")
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
