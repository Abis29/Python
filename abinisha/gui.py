from tkinter import*
root=Tk()
root.title("welcome to the page")
frame=Frame(root,bg="red",width=600,height=400)
frame.pack()
btn=Button(frame,text="livewire")
btn.pack()
root.mainloop()
from tkinter import*
root=Tk()
root.title("welcome to the page")
root=Frame(root,bg="blue",width=200,height=300)
root.grid()
lbl=Label(root,text="are you geek")
lbl.grid()
def clicked():
    lbl.configure(text="i just got clicked")
btn=Button(root,text="click me",fg="red",command=clicked)
btn.grid()
root.mainloop()
import tkinter
r=tkinter.Tk()
r.title("welcome to the page")
frame=tkinter.Frame(r,bg="blue",width=600,height=400)
frame.grid()
lbl=tkinter.Label(r,text="name")
lbl.grid()
button=tkinter.Button(r,bg="red",text="google")
button.grid(column=0,row=0)
r.mainloop()
from tkinter import*
root=Tk()
root.title("welcome to geeks for geeks")
root.geometry("350x200")
lbl=Label(root,text="are you a geek")
lbl.grid()
txt=Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    res="you wrote"+txt.get()
    lbl.configure(text=res)
btn=Button(root, text="click me",fg="red",command=clicked)
btn.grid(column=2,row=0)
root.mainloop()
# canvas
from tkinter import*
master=Tk()
master.title("welcome to my page")
w=Canvas(master,width=40,height=60)
w.pack()
canvas_height=100
canvas_width=500
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
master.mainloop()
# checkbutton
from tkinter import*
master=Tk()
var1=IntVar()
Checkbutton(master,text="male",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master,text="female",variable=var2).grid(row=1,sticky=W)
master.mainloop()
# entry
from tkinter import*
master=Tk()
Label(master,text="first name").grid(row=0)
Label(master,text="last name").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
master.mainloop()
# Frame
from tkinter import*
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text="red",fg="red")
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text="Brown",fg="brown",)
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text="blue",fg="blue")
bluebutton.pack(side=LEFT)
blackbutton=Button(bottomframe,text="black",fg="black")
blackbutton.pack(side=LEFT)
root.mainloop()
# listbox
from tkinter import*
top=Tk()
top.title("welcome to page")
frame=Frame(top,bg="red")
frame.pack()
lb=Listbox(top)
lb.insert(1,"python")
lb.insert(2,"java")
lb.insert(3,"database")
lb.insert(4,"anyother")
lb.pack()
lbl=Label(top,text="i")
top.mainloop()
from tkinter import*
top=Tk()
top.title("hello world")
top.geometry("300x400")
frame=Frame(top,bg="blue")
frame.grid()
lbl=Label(top,text="name:")
lbl.grid(column=0,row=0)
lbl=Label(top,text="age:")
lbl.grid(column=0,row=1)
btn=Button(top)
btn.grid(column=1,row=0)
btn=Button(top)
btn.grid(column=1,row=1)
top.mainloop()
#menu
from tkinter import*
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="file",menu=filemenu)
filemenu.add_cascade(label="new")
filemenu.add_command(label="open")
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label="about")
root.mainloop()
messagebox
from tkinter import*
from tkinter import messagebox
main=Tk()
ourmessage="this is our Message"
messagevar=Message(main,text=ourmessage)
messagevar.config(bg="lightgreen")
messagevar.pack()
main.mainloop()
#radio button
from tkinter import*
root=Tk()
v=IntVar()
Radiobutton(root,text="gfg",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="mit",variable=v,value=2).pack(anchor=W)
root.mainloop()
# scale
from tkinter import*
root=Tk()
w=Scale(root,from_=0,to=42)
w.pack()
w=Scale(root,from_=0,to=200,orient=HORIZONTAL)
w.pack()
root.mainloop()
from tkinter import*
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,"livewire"+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
root.mainloop()
# text
from tkinter import*
root=Tk()
T=Text(root,height=2,width=30)
T.pack()
T.insert(END,"monolisa is the\n one of famous printing\n")
root.mainloop()
# top level
from tkinter import*
root=Tk()
root.title("keerthi")
top=Toplevel()
top.title("python")
top.mainloop()
# spinbox
from tkinter import*
master=Tk()
w=Spinbox(master,from_=0,to=10)
w.pack()
mainloop()
# image
from tkinter import*
from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage
win=Tk()
win.geometry("700x500")
frame=Frame(win,width=600,height=400)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=PhotoImage(Image.open("nature.jpg"))
label=Button(frame,image=img)
label.pack()
win.mainloop()
from tkinter import*
from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage
root=Tk()
root.geometry("700x500")
frame=Frame(root,width=600,height=400)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=PhotoImage(Image.open("nature.jpg"))
frame1=Frame(root,width=600,height=400)
frame1.pack()
frame1.place(anchor="w",relx=0.5,rely=0.5)
img1=PhotoImage(Image.open("flower.jpg"))
label=Button(frame,image=img)
label.pack()
label1=Button(frame,image=img1)
label1.pack()
root.mainloop()
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    print("the name is:"+name)
    print("the password is:"+password)
    name_var.set("")
    passw_var.set("")
name_label=tk.Label(root,text="username",font=("cabibre",10,"bold"))
name_label.grid(row=0,column=0)
name_entry=tk.Entry(root,textvariable=name_var,font=("calibre",10,"normal"))
name_entry.grid(row=0,column=1)
passw_label=tk.Label(root,text="password",font=("calibre",10,"bold"))
passw_label.grid(row=1,column=0)
passw_entry=tk.Entry(root,textvariable=passw_var,font=("calibre",10,"normal"),show="*")
passw_entry.grid(row=1,column=1)
sub_btn=tk.Button(root,text="submit",command=submit)
sub_btn.grid(row=2,column=1)
root.mainloop()
import tkinter as tk
from tkinter import messagebox
def register_user():
    name=name_entry.get()
    age=age_entry.get()
    dob=dob_entry.get()
    phone=phone_entry.get()
    aadhar=aadhar_entry.get()
    pan=pan_entry.get()
    address=address_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    user_data=f"{name},{age},{dob},{phone},{aadhar},{pan},{address},{username},{password}\n"
with open("bank_data.txt","a") as file:
    file.write(user_data)
messagebox.showinfo("registration","user registered successfully!")
def login_user():
    entered_username=login_username_entry.get()
    entered_username=login_password_entry.get()
with open("bank_data.txt","r") as file:
    for line in file:
        stored_user_data=line.strip().split(",")
        stored_username=stored_user_data[0]
        stored_password==stored_user_data[1]
    if entered_username==stored_username and entered_pasword==stored_passwor:
        messagebox.showinfo("login","login successful!")
        return
messagebox.showerror("login","invalid username or password.")
window=tk.Tk()
window.title("bank statement")
window.geometry("400x600")
window.configure(bg="#ADD8E6")
tk.label(window,text="name:",bg="#ADD8E6",front=("Arial",12)).place(x=20,y=20)
name_entry=tk.Entry(window,font=("Arial",12))
name_entry.place(x=160,y=20)
tk.label(window,text="age:",bg="#ADD8E6",font=("Arial",12)).place(x=20,y=50)
age_entry=tk.Entry(window,font=("Arial",12))
age_entry.place(x=160,y=50)
tk.Label(window,text="date of birth:",bg="#ADD8E6",font=("Arial",12)).place(x=20,y=80)
dob_entry=tk.Entry(window,font= )

from tkinter import*
r=Tk()
r.geometry("400x400")
l=Label(r,text="enter the first value:")
l.grid(row=0,column=1)
l1=Label(r,text="enter the second value:")
l1.grid(row=1,column=1)
l2=Label(r,text="result:")
l2.grid(row=2,column=1)
e=Entry(r)
e.grid(row=0,column=2)
e1=Entry(r)
e1.grid(row=1,column=2)
e2=Entry(r)
e2.grid(row=2,column=2)
def add():
    a=int(e.get())
    b=int(e1.get())
    c=a+b
    e2.delete(0,END)
    e2.insert(0,c)
b=Button(r,text="add",command=lambda:add())
b.grid(row=3,column=3)
def sub():
    a=int(e.get())
    b=int(e.get())
    c=a-b
    e2.delete(0,END)
    e2.insert(0,c)
b1=Button(r,text="sub",command=lambda:sub())
b1.grid(row=4,column=3)
def mul():
    a=int(e.get())
    b=int(e.get())
    c=a*b
    e2.delete(0,END)
    e2.insert(0,c)
b2=Button(r,text="mul",command=lambda:mul())
b2.grid(row=5,column=3)
r.mainloop()
a=123456
a1=a
c=0
while (a1>0):
    r=a1%10
    c=(c*10)+r
    a1=a1//10
print(c)
a==c:
print("it is a palindrome")
else=int(input("enter the number:"))
b=a
c=0
while (b>0):
    r=b%10
    c=(c*10)+r
    b=b//10
print(c)
if a:
    print("it is not a palindrome")
a=input("enter the name:")
b=a[::-1]
if a==b:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
num=int(input("enter the number:"))
a=num
b=a*(a)
c=0
while(b>0):
    r=b%10
    c=(c*10)+r   
    b=b//10
print(c)
print(b)
if c==b:
    print("it is adam number")
else:
    print("it is not adam number")
number=int(input("enter the first value:"))
s1=number
squr=s1*s1
value1=0
while(squr>0):
    r=squr%10
    value1=(value1*10)+r
    squr=squr//10
print(value1)
temp=0
while(s1>0):
    r=s1%10
    temp=(temp*10)+r
    s1=s1//10
print(temp)
value2=temp*temp
print(value2)
if (value1==value2):
    print("adam number")
else:
    print("not adam number")
a=int(input("enter the number:"))
num=a
b=num*num*num
print(b)
c=int(input("enter the number"))
num=c
d=0
while(num>0):
    r=num%10
    d=d+(r**3)
    num=num//10
print(d)
if d==c:
    print("amstrong number")
else:
    print("not aamstrong number")

from kk import  *
a=int(input("enter the value:"))
if reverse(val(a))==val(reverse(a)):
    print("it is adam no")
else:
    print("not adam no")
#fibonacci series
num=int(input("enter the value:"))
a=0
b=1
for i in range(num):
    a=(a)
    c=(a)
    a=b
    b=c+b
print(b)
a=int(input("enter the value:"))
f1,f2=0,1 
f3=f1+f2
print("fibonacci no",a)
print(f1)
print(f2)
for i in range(5):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2
#factorial
# sum=int(input("enter the number"))
def fact(sum):
    fact=1
    sum=int(input("enter the number"))
    for i in range(1,sum+1):
      fact=fact*i
    return fact
print("factorial value",fact(sum))
# num=int(input("enter a number:"))
fact=1
if num<0:
    print("factorial does not exist for negative")
elif num==0:
    print("the factorial of o is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("the facorial of",num,fact)
def pali(c):
    a=int(input("enter the value:"))
    b=a*a
    while(b>0):
        r=b%10
        c=(c*10)+r
        b=b//1
        print(c)
        print(b)
    if c==b:
        print("it is adam number")
    else:
        print("it is not adam number")
def amstrong(b):
    num=a
    b=num*num*num
    print(b)
    num=c
    d=0
    while(num>0):
        r=num%10
        d=d+(r**3)
        num=num//10
        print(d)
    if d==c:
        print("amstrong number")
    else:
        print("not aamstrong number")
def palindrome(c):
    b=a
    c=0
    while (b>0):
        r=b%10
        c=(c*10)+r
        b=b//10
        print(c)
    if a==c:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
def fibonacci(c):
    f1,f2=0,1 
    f3=f1+f2
    print("fibonacci no",a)
    print(f1)
    print(f2)
    for i in range(5):
        print(f3)
        f1=f2
        f2=f3
        f3=f1+f2
def fact(c):
    for i in range(1):
      fact=fact*i
    return fact
print("factorial value",fact(c))
def palin(c):
    b=a[::-1]
    if a==b:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
n=int(input("enter your choice1.adam\n2.amstrong\n,3.palindrome\n4.fibonacci\n5.factorial\n6.palin"))
c=int(input("enter your number"))
if n==1:
    adam(c)
elif n==2:
    amstrong(c)
elif n==3:
    palindrome(c)
elif n==4:
    fibonacci(c)
elif n==5:
    fact(c)
elif n==6:
    palin(c)
else:
    print("please enter the correct input")

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
c=1
while(c==1):
    n=int(input("enter your choice1.add\n2.sub\n3.mul\n4.div\n5.mod"))
    a=int(input("enter the first value:"))
    b=int(input("enter the second value:"))
    if (n==1):
        add(a,b)
    elif (n==2):
        sub(a,b)
    elif (n==3):
        mul(a,b)
    elif (n==4):
        div(a,b)
    elif (n==5):
        mod(a,b)
    else:
        print("enter correct value")
    c=int(input("if you want continue,please enter 1?"))
def adam(a):
    dup=a 
    squ1=dup*dup
    firstvalue=0
    while(squ1>0):
       r=squ1%10
       firstvalue=(firstvalue*10)+r
       squ1=squ1//10
    temp=0
    while(dup>0):
       r=dup%10
       temp=(temp*10)+r
       dup=dup//10
       secondvalue=temp*temp
       print(temp)
def amstrong(a):
    num=a
    d=0 
    while(num>0):
       r=num%10
       d=d+(r**3)
       num=num//10
       print(d)
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
c=1
while(c==1):
    n=int(input("enter the choice\n1.adam\n2.amstrong\n3.fact"))
    a=int(input("enter the value"))
    if (n==1):
        adam(a)
        print("it is adam number")
    elif (n==2):
        amstrong(a)
        print("it is amstrong number")
    elif (n==3):
        fact(a)
        print("it is factorial",fact(a))
    else:
# #         print("please enter correct value")
     string=input("enter the string")
number=string[2]
if (number=="a"):
    a=int(input("enter the value"))
    if a%2==0:
        print("even number")
    else:
        print("odd number")
elif (string[0]=="b"):
    from  kk import*
    if adam(val(a)==val(adam(a))):
        print("it is adam number")
    else:
        print("it is not adam number")
else:
    print("it is not a")
string=input("enter the string:")
if (string=="bhavyadharshini"):
    b=string[3:9].upper()

    print(b[0:2],b[2:4],b[4:7],sep='***')
else:
#     print("does not correct value")
   string="pythonprogramming"
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
least_freq=[]
for i in freq:
    if freq[i]==1:
        least_freq.append(i)
print(least_freq)
n=int(input("enter your value:"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
if count==1:
    print("prime")
else:
    print("not")
# ascending order
list=[2,6,5,9,4,1,6,0]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
value=int(input("enter your value:"))
while value<5:
    value=value+1
    val=(value**3)-1
    print(val)
list1=[0,1,2,3,4,5]
b=list1.copy()
b.sort()
if list1==b:
    x=map(lambda a:a*2,list1)
    print(list(x))
else:
#     print("does not ascending")
      rows=int(input("enter the value"))
for i in range(1,rows+1):
    for j in range(i,i+1):
        print("*"*i)
x=1
for i in range(9):
    if i<4:
        print("*"*x)
        x+=1
    elif i>3:
        print("*"*x)
        x=x-1
value="bhavya"
for i in range(6):
    if i<5:
        print(value)
        value+=value
n=int(input("enter no:"))
for i in range(n,0-1):
    for j in range(i):
        print("*",end="")
    print()


# registration form
from tkinter import*
root=Tk()
file=open('form.txt','a')
root.title("registration form ")
root.geometry("200x300")
frame=Frame(root)
frame.grid()
l1=Label(root,text="Name:")
l1.grid(row=0,column=0)
l2=Label(root,text="Class:")
l2.grid(row=1,column=0)
l3=Label(root,text="Age:")
l3.grid(row=2,column=0)
l4=Label(root,text="Department:")
l4.grid(row=3,column=0)
l5=Label(root,text="College Name:")
l5.grid(row=4,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
e3=Entry(root)
e3.grid(row=2,column=1)
e4=Entry(root)
e4.grid(row=3,column=1)
e5=Entry(root)
e5.grid(row=4,column=1)
def click():
    l1=e1.get()
    l2=e2.get()
    l3=e3.get()
    l4=e4.get()
    file=open("form.txt","a")
    file.write(l1+l2+l3+l4)

button=Button(root,text="enter",command=click)
button.grid(row=5,column=2)
root.mainloop()
username="name"
password="paswd"
f=open("new1.txt","r")
data1=f.read()
lines=data1.split("\n")
for line in lines:
    info=line.split()
    if info[0]==username and info[1]==password:
        print("logged in")
        break
else:
    print("nothing")
from tkinter import*
root=Tk()
root.geometry("500x500")
l1=Label(root,text="name")
l1.grid(row=0,column=2)
e1=Entry(root)
e1.grid(row=0,column=3)
l2=Label(root,text="age")
l2.grid(row=1,column=2)
e2=Entry(root)
e2.grid(row=1,column=3)
l3=Label(root,text="address")
l3.grid(row=2,column=2)
e3=Entry(root)
e3.grid(row=2,column=3)
l4=Label(root,text="email")
l4.grid(row=3,column=2)
e4=Entry(root)
e4.grid(row=3,column=3)
l5=Label(root,text="phoneno")
l5.grid(row=4,column=2)
e5=Entry(root)
e5.grid(row=4,column=3)
l6=Label(root,text="marks")
l6.grid(row=5,column=2)
e6=Entry(root)
e6.grid(row=5,column=3)
l7=Label(root,text="gender")
l7.grid(row=6,column=2)
e7=Entry(root)
e7.grid(row=6,column=3)
var=IntVar()
Radiobutton(root,text="male",variable=var,value=5).grid(row=7,sticky=W)
Radiobutton(root,text="female",variable=var,value=2).grid(row=8,sticky=W)
def note():
    l11=e1.get()
    l12=e2.get()
    l13=e3.get()
    l14=e4.get()
    l15=e5.get()
    l16=e6.get()
    l17=e7.get()
    gen=""
    if var==1:
       gen="male"
    else:
       gen="female"
    f=open("file.txt","a")
    f.write(l11+" "+l12+" "+l13+" "+l14+" "+l15+" "+l16+" "+l17+" "+gen)
b=Button(root,text="submit",command=note)
b.grid(row=8,column=4)
root.mainloop()
from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("login form")
root.geometry("500x500")
l1=Label(root,text="username")
l1.place(relx=0.1,rely=0.2)
e=Entry(root)
e.place(relx=0.3,rely=0.2)
l2=Label(root,text="password")
l2.place(relx=0.1,rely=0.3)
e1=Entry(root)
e1.place(relx=0.3,rely=0.3)
def data():
    l1=e.get()
    l2=e1.get()
    username=""
    if username=="bhavya":
        print("login successfuly")
    else:
        print("incorrect")
    f=open("user.txt","a")
    f.write(l1+""+l2+"")
b=Button(root,text="submit",command=data)
b.place(relx=0.3,rely=0.5)
root.mainloop()
# radiobutton
from tkinter import*
def sel():
    selection="you selected the option"+str(var.get())
    Label.config(text=selection)
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
r1.pack()
r2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
r2.pack()
r3=Radiobutton(root,text="option3",variable=var,value=3,command=sel)
r3.pack()
label=Label(root)
label.pack()
root.mainloop()
checkbutton
from tkinter import*
r=Tk()
var=IntVar()
c=Checkbutton(r,text="new1",variable=var).pack()
var2=IntVar()
c1=Checkbutton(r,text="new2",variable=var2).pack()
var3=IntVar()
c2=Checkbutton(r,text="new3",variable=var3).pack()
r.mainloop()
#combobox
from tkinter import*
from tkinter import ttk
root=Tk()
root.title("combobox")
root.geometry("300x300")
combo=ttk.Combobox(root,values=(["option1"],["option2"],["option3"],["option4"],["option5"]))
combo.pack()
def option_selected(event):
    selected_option=combo.get()
    print("you selected:",selected_option)
combo.bind("<<<combobox selected>>",option_selected)
root.mainloop()
from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("bank")
frame=Frame(root,width=1000,height=1000)
frame.pack()
frame1=Frame(root,width=1000,height=1000,bg="pink")
label=Label(root,text="SBI BANK",font=("Times New Roman",20),bg="green")
label.place(relx=0.43,rely=0.01)
button=Button(root,text="Customer Registration",bg="pink")
button.place(relx=0.4,rely=0.49)
button1=Button(root,text="admin login",bg="pink")
button1.place(relx=0.5,rely=0.59)
button2=Button(root,text="customer login",bg="pink")
button2.place(relx=0.6,rely=0.69)
s="A bank is a financial institution that accepts that deposits and public"
label1=Label(root,text=s,font=("Times New Roman",15))
label1.place(relx=0.2,rely=0.2)
frame1.pack()
root.mainloop()



    
    






    






    









