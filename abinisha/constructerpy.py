# class student:
#     def __init__(self):
#         name="abis"
#         age=23
#         salary=1000
#         designation="developer"
#         print("name:",name)
#         print("age:",age)
#         print("salary:",salary)
#         print("designation:",designation)
# obj=student()
# class person:
#     def __init__(self):
#         print("1")
#     def __init__(self):
#         print("2")
# p1=person()
# p2=person()
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def print(self):
#         print("my name is:",self.name)
#         print("my age is:",self.age)
# obj=student("john",23)
# obj=student("jith",21)
# obj.print()
# class student():
#     def studentdetails(self):
#         print("It is my details")
#         print("It is my details")
# class staff(student):
#         def staffdetails(self):
#             print("yeah its me")
# detail=staff()
# detail.studentdetails()
# detail.staffdetails()
# class employeedetails():
#      def company(self,name,age):
#           print("It is my resume")
#           print("name:",name,"age:",age)
# class secondround():
#      def round2(self,score):
#           print("It is my score")
#           print("my score is:",score)
# class thirdround(employeedetails,secondround):
#      def round3(self,hr):
#           print("final round")
#           print("my details",hr)
# obj=thirdround()
# obj.company("jith",23)
# obj.round2(24)
# obj.round3("sss")


# single inheritance
class vehicle:
     def vehicle_info(self):
          print("inside vehicle class")
class car(vehicle):
     def car_info(self):
          print("inside car class")
car=car()
car.vehicle_info()
car.car_info()

class person():
     def person_info(self,name,age):
          print("inside person class")
          print("name:",name,"age",age)
class company():
     def company_info(self,company_name,location):
          print("inside company class")
          print("name:",company_name,"location:",location)
class employee(person,company):
     def employee_info(self,salary,skill):
          print("inside employee class")
          print("salary:",salary,"skill:",skill)
emp=employee()
emp.person_info("abinisha",23)
emp.company_info("fibro","myd")
emp.employee_info(2000,"machine learning")


