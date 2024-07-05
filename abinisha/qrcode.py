# import qrcode
# img=qrcode.make("vanakkam thamizha")
# img.save("1.jpg")

# import cv2
# qr_img=cv2.imread("1.jpg")
# qr_det=cv2.QRCodeDetector()
# val,pts,st_code=qr_det.detectAndDecode(qr_img)
# print("information:",val)



# guitext
from tkinter import *
root=Tk()
text=Text(root,height=2,width=30)
text.insert(INSERT,"hello....")
text.insert(END,"kitty....")
text.pack()
b=Button(root,text='click')
b.pack()
text.tag_add("here","1.0","1.4")
text.tag_add('start','1.8','1.10')
text.tag_config("here",background="green",foreground="violet")
text.tag_config('start',background='blue',foreground='yellow')
root.mainloop()





# iterator
mytuple=("cs","msc","mca")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))





# arithmetic operator
import tkinter
from tkinter import *
from tkinter import messagebox

r=Tk()
r.geometry("400x400")
l1=Label(r,text="Enter the first value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="Result")
l3.grid(row=2,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.delete(0,50)
    e3.insert(0,c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.delete(0,50)
    e3.insert(0,c)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.delete(0,50)
    e3.insert(0,c)
def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    e3.delete(0,50)
    e3.insert(0,c)
    messagebox.showinfo("textbox","valid-successfully")

b=Button(r,text="Sub",bg="pink",command=lambda:sub())
b.grid(row=0,column=3)

b=Button(r,text="Add",bg="red",command=lambda:add())
b.grid(row=1,column=3)

b=Button(r,text="Mul",bg="green",command=lambda:mul())
b.grid(row=2,column=3)

b=Button(r,text="Div",bg="yellow",command=lambda:div())
b.grid(row=3,column=3)

r.mainloop()