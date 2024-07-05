#pop item at the given index from thelist
languages=["python","java","french","c++"]
return_value=languages.pop(3)
print(return_value)
print("updated list",languages)
#remove and return the last item
print("when index is not paused:")
print("return value:",languages.pop())
print("updated list:",languages)
#use of count
vowels=["apple","banana","cherry"]
count=vowels.count("apple")
print("the count is:",count)
#random tuple and list elements
random=["a",("a","b"),("a","b"),[3,4]]
count=random.count(("a","b"))
print("the count of [(a,b)] is:",count)

count=random.count([3,4])
print("the count of [3,4] is:",count)
numbers=[87,89,64,12,11,2]
numbers.sort()
print(numbers)
fruits=["apple","mango","cherry"]
fruits.sort(reverse=True)
print("sorted list:",fruits)
#tuple
details=["student","mark","rank","students","mark"]
print(details)
#tuple length
fruits=["apple","mango","cherry"]
print(len(fruits))
#tuple with one item
tuple=("car")
print(type(tuple))
tuple1=(4,5,6)
print(type(tuple1))
tuple2=("apple","mango")
print(type(tuple2))
tuple3=(True,False,False)
print(type(tuple3))
tuple1=("apple","banana")
tuple2=(3,4,5)
tuple3=(True,False,False)
print(tuple1,tuple2,tuple3)
#set
mixed_set={"hello",101,-2,"bye"}
print("print mixed sets",mixed_set)
#duplicate
numbers={1,2,3,4,5,6,7,7,6,5,1,1}
print(numbers)
#empty
empty_dictionary={}
print("print the empty",empty_dictionary)
#add items
numbers={12,23,45,67}
print(numbers)
numbers.add(49)
print("added set",numbers)
#update python set
companies={"lacoste","ralph","vibro"}
remove=companies.discard("vibro")
print(companies)
#for loop
animals={"cat","dog","elephant"}
for x in animals:
    print(x)
#find numbers
num={1,2,3,4}
print("the set is",num)
print("total elements",len(num))
#set operation
A={1,2,3,4}
B={4,5,6,7}
print("union using union():",A.union(B))
#set intersection
A={1,2,3,4}
B={2,3,4,5}
print("intersection using intersection():",A.intersection(B))
print("difference using&:",A-B)
print("using^:",A^B)
print("using symmetric_difference():",A.symmetric_difference(B))
A={1,2,3}
B={2,3,4}
if A==B:
    print("set A and set B are equal")
else:
    print("set A and set B are not equal")
#creating a dictionary
country_capitals={
    "united states":"washington",
    "italy":"rome",
    "england":"london"
    }
print(len(country_capitals))
#access dictionary items
country_capitals={
    "united states":"washington",
    "italy":"nepals",
    "england":"london"
    }
country_capitals["italy"]="nepals"
print(country_capitals)
#add items to a dictionary
country_capitals={
    "united states":"washington",
    "italy":"nepals"
    }
country_capitals["germany"]="berlin"
print(country_capitals)
del country_capitals["united states"]
print(country_capitals)
person={"name":"phil","age":22,"salary":3500.0}
print("person=",person)
person["profession"]="plumber"
result=person.popitem()
print("return value=",result)
print("person=",person)
fruits_name={"apple","banana","cherry"}
fruits_name.popitem()
print("fruits=",fruits_name)
