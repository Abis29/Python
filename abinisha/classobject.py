# class students():
#     def __init__(self,mark,result):
#         self.mark=mark
#         self.result=result
#     def demo(self):
#         print("total marks is: ",self.mark)
#         print("Result: ",self.result)
# obj1=students(78,230)
# obj2=students(90,250)
# obj3=students(40,590)
# obj1.demo()
# obj2.demo()
# obj3.demo()           

# var="apple"
# myiter=iter(var)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# def var():
#     n=1
#     while n<10:
#         val=n*n
#         yield val
#         n+=1
# a=var()
# for i in a:
#     print(i)   

# def greet(name):
#     def display_name():
#         print('hello',name)
#     display_name
# greet('ammu')
# def greet():
#     name='ammu'
#     return lambda:'hello'+name
# message=greet()
# print(message())
def outer(x):
    def inner(y):
        return x/y
    return inner
x=outer(5)
y=x(4)
print(y)