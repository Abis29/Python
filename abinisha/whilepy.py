# while
i=3
n=5
while i<n:
 print
age=45
counter=int(input("enter your number:"))
while counter<3:
 print("inside loop")
 counter=counter+1
 print("counter")
else:
 print("inside statement")
 
i=2
j=5
while i<=4:
    while j<8:
        print(i,",",j)
        j=j+1
        i=i+1
        
i=1
while i<=5:
    j=2
    while j<=5:
        print(i,"*",j,"=",i*j)
        i=i+1
        print("\n")    
a="bhavya"
for i in a:
    print(i)
for x in range(1,20,3):
    print(x)
a=["happy",2,6]
for i in a:
    print(i)
list1=[1,2,3,4]
sum=0
for i in list1:
    sum=sum+i
    print("the total value is:",sum)
   
i=3
n=5
while i<n:
   print(i)
   i=i+1
counter=int(input("enter your number:"))
while counter<3:
   print("inside loop")
   counter=counter+1
   print("counter")
else:
   print("inside statement")

def myfunction():
   print("hello world")
myfunction()
def addnum(num1,num2):
   print(num1+num2)
addnum(2,3)
def function(name,age):
   print(name,age)
function("livewire",23)
def multiplynum(num1):
 return num1*7
result=multiplynum(8)
print(result)
#recursion

def factorial(x): 
   if x==1:
    return 1
   else:
    return (x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial(num))
i=1
while i<=10:
  j=2
  while j<=2:
     print(i,"*",j,"=",i*j)
     i+=1
     j+=1
     print("\n")
year=int(input("enter leap year:"))
if(year%400==0)and(year%100==0):
 print("{} is a leap year".format(year))
elif(year%4==0)and(year%100!=0):
   print("{} is a leap year".format(year))
else:
     print("{} is not a leap year".format(year))
num=int(input("enter your number:"))
if num%2==0:
  print("even number")
else:
  print("odd number")