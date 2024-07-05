# class student():
#    def stdname(self,name1):
#       print("name:",name1)
# class college(student):
#    def clgname(self,name2):
#       print("clgname:",name2)
# class department(college):
#    def depname(self,name3):
#       print("depname:",name3)
# project=department()
# project.stdname("bhavya")
# project.clgname("dgga")
# project.depname("cs")
# class covid19():
#     def patients(self,count,certify):
#         print("peoples affect in covid19:",count,certify)
# class covid20():
#     def patients2(self,count1,certify2):
#         print(" peoples death in covid20:",count1,certify2)
#         print(" peoples birth in covid20:",count1,certify2)
# class covid21():
#     def patients3(self,count3,certify3):
#         print("peoples recovered in covid21:",count3,certify3)
# class covid22(covid19,covid20,covid21):
#     def patients4(self,count4,certify4):
#         print("peoples are cured in covid22:",count4,certify4)
# lockdown=covid22()
# lockdown.patients(100,"positive")
# lockdown.patients2(50,"positive")
# lockdown.patients2(50,"negative")
# lockdown.patients3(40,"positive")
# lockdown.patients4("all","negative")
# class student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def details(self):
#         print(f"am a student.my name is {self.name}.am {self.age} years old")
#     def info(self):
#         print("marks")
# class staff():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def details(self):
#         print(f"am a staff.my name is {self.name}.am {self.age} years old")
#     def info(self):
#         print("marks")
# obj1=student("abi",24)
# obj2=staff("sumi",40)
# obj1.details()
# obj1.info()
# obj2.details()
# obj2.info()
# class employee():
#     def __init__(self,employeename,salary,qualification):
#         self.employeename=employeename
#         self.salary=salary
#         self.qualification=qualification
#     def details(self):
#         print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
# class hr():
#     def __init__(self,employeename,salary,qualification):
#         self.employeename=employeename
#         self.salary=salary
#         self.qualification=qualification
#     def details(self):
#         print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
# obj=employee("bhavya",23455,"b.sc")
# obj2=hr("abi",23145,"m.sc")
# obj.details()
# obj2.details()
# #super function
# class parent():
#     def fun(self):
#         print("they are aprent of arshi:")
# class child(parent):
#     def fun1(self):
#         super().fun()
#         print("theya re the best parent")
# obj=child()
# obj.fun1()
#abstract method
# from abc import ABC, abstractmethod
# class bank(ABC):
#     def bank_info(self):
#         print("welcome to bank")
#     @abstractmethod
#     def interest(self):
#         "abstract method"
#         pass
# class SBI(bank):
#     def interest(self):
#         print("5 percentage")
# s=SBI()
# s.bank_info()
# s.interest()
# import tkinter
# top=tkinter.Tk()
# top.mainloop()
# from tkinter import*
# root=Tk()
# frame=Frame(root,bg="red",width=500,height=400)
# f=Button(root,bg="blue")
# f.pack()
# frame.pack()
# root.mainloop()
import tkinter
t=tkinter.Tk()
f1=tkinter.Frame(t)
f2=tkinter.Frame(t)
l=tkinter.Label(f1,text="hello",bg="blue")
l.pack()
b=tkinter.Button(f2,text="livewire")
b.pack()
f1.pack(padx=50,pady=90)
f2.pack(padx=60,pady=50)
t.mainloop()

    
