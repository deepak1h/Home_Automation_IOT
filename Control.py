import tkinter
import time
from tkinter import messagebox
from tkinter import *
def control():

    #import RPi.GPIO as device



    #f=2
    #a=2
    #l=3
    #m=4



    #device.setwarnings(False)
    #device.setmode(device.BCM)
    #device.setup(f,device.OUT)
    #device.setup(a,device.OUT)
    #device.setup(l,device.OUT)
    #device.setup(m,device.OUT)





    def b1():
    #    device.output(f,True)
        print("Fan ON")
    def b2():
    #    device.output(f,False)
        print("Fan OFF")
    def b3():
    #    device.output(a,True)
        print("AC ON")
    def b4():
    #    device.output(a,False)
        print("AC OFF")
    def b5():
    #    device.output(l,True)
        print("Lights ON")
    def b6():
    #    device.output(l,False)
        print("Lights OFF")
    def b7():
    #    device.output(m,True)
        print("Main Power ON")
    def b8():
    #    device.output(m,False)
        print("Main Power OFF")





    home=tkinter.Tk()
    home.title("Home Control")
    home.geometry("1366x768")
    home["bg"]="#3c4250"
    home["bd"]=33



    f1=Frame(home,bg="#424242",height=700,width=1300,bd=5,)
    f1.pack()




    l1=Label(f1,text="HOME CONTROL",font=("arial",40),bg="#424242",fg="white")
    l1.place(x=400,y=0)
    l2=Label(f1,text="Fan",font=("arial",30),bg="#424242",fg="white")
    l2.place(x=300,y=150)
    l3=Label(f1,text="AC",font=("arial",30),bg="#424242",fg="white")
    l3.place(x=300,y=250)
    l4=Label(f1,text="Lights",font=("arial",30),bg="#424242",fg="white")
    l4.place(x=300,y=350)
    l5=Label(f1,text="Main power",font=("arial",30),bg="#424242",fg="white")
    l5.place(x=300,y=450)




    b1=Button(f1,text="ON",font=("arial",20),bg="black",fg="white",command=b1)
    b1.place(x=700,y=150)
    b2=Button(f1,text="OFF",font=("arial",20),bg="black",fg="white",command=b2)
    b2.place(x=800,y=150)
    b3=Button(f1,text="ON",font=("arial",20),bg="black",fg="white",command=b3)
    b3.place(x=700,y=250)
    b4=Button(f1,text="OFF",font=("arial",20),bg="black",fg="white",command=b4)
    b4.place(x=800,y=250)
    b5=Button(f1,text="ON",font=("arial",20),bg="black",fg="white",command=b5)
    b5.place(x=700,y=350)
    b6=Button(f1,text="OFF",font=("arial",20),bg="black",fg="white",command=b6)
    b6.place(x=800,y=350)
    b7=Button(f1,text="ON",font=("arial",20),bg="black",fg="white",command=b7)
    b7.place(x=700,y=450)
    b8=Button(f1,text="OFF",font=("arial",20),bg="black",fg="white",command=b8)
    b8.place(x=800,y=450)



    home.mainloop()
control()
