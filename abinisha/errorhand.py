#error handling
divide_numbers=7/0
print(divide_numbers)
print(dir(locals()["_builtins"]))
file=open("new.txt","a")
file.write("\nemp name\tage\tsalary\tqualifi")
file.write("\nanbu\t23\t2000\tdme")
file.write("\nakash\t21\t3000\tb.sc")
file.write("\nbijorn\t24\t4000\tdme")
file.write("\nvishwa\t20\t1000\tdme")
file.write("\najay\t21\t1200\tb.com")
file.close()
with open("new.txt","r") as file:
    data=(file.read())
print(data)
class myclass():
    x=5
print(myclass)
class name():
    x=4
ob=name()
print(ob.x)
class add():
    a=5
    b=4
    c=a+b
ob=add()
print(ob.c)
class sub():
    x=int(input("enter a num:"))
    y=int(input("enter b num:"))
    z=x+y
ob=sub()
print(ob.z)
class addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("first number="+str(self.first))
        print("second number="+str(self.second))
        print("addition of two numbers="+str(self.answer))
    def calculate(self):
        self.answer=self.first+self.second
obj1=addition(100,200)
obj2=addition(20,20)
obj1.calculate()
obj2.calculate()
obj1.display()
obj2.display()
class mult():
    x=10
    y=2
    z=x*y
print(mult.z)
class function():
    x=int(input("enter a number:"))
    y=int(input("enter b number:"))
    z=x//y
ob=function()
print(ob.z)



#exception handling
try:
    file1=open("newi.txt","r")
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print("filenot found errorsuccessfully handled")
          
