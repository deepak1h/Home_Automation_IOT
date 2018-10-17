import tkinter
from tkinter import *
from tkinter import messagebox
import urllib3
import json
import random
http = urllib3.PoolManager()
def forget():

    root=tkinter.Tk()
    root.geometry("1366x768")
    root["bg"]="black"
    root["bd"]="30"
    root.title("Forget page")

    f1=Frame(root,height=700,width=1300,bg="#454545")
    f1.pack()
    def check():
            o=e8.get()
            if OT==o:
                l6=Label(f1,text="Name: "+nm,font=("ubuntu",30),bg="#454545",fg="white")
                l6.place(x=400,y=400)
                l4=Label(f1,text="user ID: "+id1,font=("ubuntu",30),bg="#454545",fg="white")
                l4.place(x=400,y=450)
                l5=Label(f1,text="password: "+pss,font=("ubuntu",30),bg="#454545",fg="white")
                l5.place(x=400,y=500)

                
            else:
                messagebox.showinfo(title="ERROR", message="OTP not match")

    
    def otp():
        global OT
        OT=str(random.randint(1000,9999))
        r1=http.request('GET',"https://smsapi.engineeringtgr.com/send/?Mobile=7376182917&Password=7376182917&Message="+"OTP="+OT+"&To="+mob+"&Key=deepa8GWw9z3Ur0DvVZEJaTyeiq")
        data2 = r1.data.decode('utf-8')
        if "true" in data2:
            messagebox.showinfo(title="Alert", message="OTP sent to your Mobile")
            l9 = Label(f1, text="OTP", font=("ubuntu", 20), bg="#424242", fg="white")
            l9.place(x=500, y=300)
            global e8
            e8 = Entry(f1, bg="white", bd=1, width=10, font=("URW gothic L", 15, "bold"))
            e8.place(x=620, y=300)
            b2 = Button(f1, text="Submit", font=("ubuntu", 20), command=check)
            b2.place(x=500, y=350)
            b2 = Button(f1, text="Resend", font=("ubuntu", 20), command=otp)
            b2.place(x=700, y=350)
            
        elif "finished your day quota." in data2:
            messagebox.showinfo(title="Alert", message="unable to send Try again after 24 hr.")
            root.destroy()
            Login_Page.log()
            
        else:
            messagebox.showinfo(title="Alert", message="unable to send OTP, retry")


           

        
    def query():
        r=http.request('GET',"https://deepakkumarpandeychs.000webhostapp.com/getstatus2.php")
        data = r.data.decode('utf-8')
        data=data[2:-2].split("},{")
        lst=list()
        global mob,id1,pss,nm
        id1=e1.get()
        mob=e2.get()
        for i in data:
            lst.append(i.split(","))
        data=[]
        for i in lst:
            p=[i[0][8:-1],i[1][12:-1],i[2][8:-1],i[3][10:-1]]
            data.append(p)
            p=[]
            l=0
        for i in data:
            l+=1
        
            if (id1==i[0] and mob==i[3]):
                pss=i[1]
                nm=i[2]
                otp()
                break

            elif l==len(data):
                messagebox.showinfo(title="Error", message="Input Data Not Match")

    l1=Label(f1,text="Forget Password",font=("ubuntu",30),bg="#454545",fg="white")
    l1.place(x=500,y=50)
    l2=Label(f1,text="User ID*",font=("ubuntu",20),bg="#454545",fg="white")
    l2.place(x=400,y=150)
    l3=Label(f1,text="Mobile No*",font=("ubuntu",20),bg="#454545",fg="white")
    l3.place(x=400,y=200)
    global e1,e2
    e1=Entry(f1,bg="white",width=25,font=("URW gothic L",15,"bold"))
    e1.place(x=600,y=150)
    e2=Entry(f1,bg="white",width=25,font=("URW gothic L",15,"bold"))
    e2.place(x=600,y=200)


    b1=Button(f1,text="Forget",command=query,font=("ubuntu",15))
    b1.place(x=650,y=250)

    root.mainloop()
