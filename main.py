##print
#print("pizza")
#print("its good")
##variables
##string
#name = "Naman"
#print(f"my name is {name} ")
##int
#age = 20
#print(f"my age is {age} ")
##float
#price = 60.75
#print(f"price of dozen apple is {price} rupees")
##boolean
#is_Student = True
#if is_Student:
#    print("true")
#else:
#    print("false")
##type casting and also displaying data type
#name = "Naman"
#age = 20
#gpa = 7.5
#is_Student = True
#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(is_Student))
#gpa = int(gpa)
#print(gpa)
#
##taking input it store data as string even numbers so convert for arithematic
#name = input("enter name?:")
#age = input("enter age?:")
#print (f"hello {name}!!! ")
#print(f"you are {age} yr old!!!")
#
##Area calculator rectangle
#length = int(input("enter length?:"))
#breadth = int(input("enter breadth?:"))
#area = length * breadth
#print(f"the area is :{area}cm²")
#
##item cart
#item = input("what do u want?:")
#quantity = int(input("how many u want?:"))
#price = float(input("the price :"))
#total = quantity*price
#print(f"U bought {quantity} x {item}/s")
#print(f"$ {total}" )

#madlib game
#word1 = input("enter word 1:")
#word2 = input("enter word 2:")
#word3 = input("enter word 3:")
#print(f"today i went to {word1} zoo")
#print(f"there i saw {word2}")
#print(f"i was {word3} when i saw {word2}")

#SOME BASIC FUNCTION
#x = 20
#y = 3.256
#z = 5
#result1 = round(y)
#print(result1)
#result2 = abs(x)
#print(result2)
#result3 = pow(5,4)
#print(result3)
#result4 = max(x,y,z)
#print(result4)
#result5 = min(x,y,z)
#print(result5)

#some math function
#import math
#x = 25
#print(math.e)
#print(math.pi)
#result = math.sqrt(x)
#print(result)
#y = 9.75
#result1 = math.ceil(y)
#print(result1)
#result2 = math.floor(y)
#print(result2)

#circumference and area of circle
#radius = float(input("enter radius:"))
#c = 2*math.pi*radius
#print(f"{c} cm")
#a = math.pi * pow(radius,2)
#print(f"{a} cm^2")

#math expression c = root(a^2 + b^2)
#a = float(input("enter a :"))
#b = float(input("enter b :"))
#c = math.sqrt(pow(a,2) + pow(b,2))
#print(c)

#loops
#if
#age = int(input("enter your age:"))
#if age<18:
#    print("NOT ELIGIBLE TO VOTE")
#else:
#    print("ELIGIBLE TO VOTE")

#response = input("do u want to exit?  (Y/N):")
#if response == "Y":
#    print("u can go!!")
#else:
#    print("ok fine wait")

#name = input("Enter Name:")
#if name =="":
#    print("Please enter name")
#else:
#    print(f"hi {name}")

#basic calculator using if 
#operator = input("SELECT +,-,*,/  :")
#a = float(input("enter first number : "))
#b = float(input("enter second number : "))
#if operator == "+":
#    result = a + b
#    print(result)
#elif operator == "-":
#    result = a - b
#    print(result)
#elif operator == "*":
#    result = a * b
#    print(result)
#elif operator == "/":
#    result = a / b
#    print(result)
#else :
#    print("INVALID")
    
#weight convertor
#to_convert = input("Select kg or gm : ")
#weight = float(input("enter weight : "))
#if to_convert == "kg":
#    gram = weight * 1000
#    print(gram)
#else:
#    kg = weight /1000
#    print(kg)

#temp convertor

#select = input("select to covert from (c/f) : ")
#temp = float(input("Enter Temp:"))
#if select == "c":
#    temp = round((9*temp)/ 5 +32,1)
#    print(temp)
#else:
#    temp = round((temp-32)*5/ 9,1)
#    print(temp)

#and, or ,not

#is_single = True
#age = int(input("enter age: "))
#if age>21 and is_single:
#    print("SHaadi")
#else:
#    print("no Shaadi")    

#ternary operator X if condition else Y

#age = 25
#print("aduld"if age >18 else "child")
#num =26
#print("Even" if num%2 == 0 else "odd")

# String method
#SSname = input("ENTER YOUR NAME: ")
#result = len(name)
#print(result)
#
#result1 = name.find("a")
#print(result1)
#
#result2 = name.rfind("n")
#print(result2)

#name = name.capitalize()
#print(name)
#name = name.upper()
#print(name)
#name = name.lower()
#print(name)
#name = name.isdigit()
#print(name)
#name = name.isalpha()
#print(name)
#result = name.count("n")
#print(result)
#result = name.replace("n","b")
#print(result)

#basic validation
#username = input("enter username : ")
#
#if len(username)>12:
#    print("enter less than 12 characters")
#elif not username.find(" ") == -1:
#    print("NO SPACE ALLOWED")
#elif not username.isalpha():
#    print("no digits allowed")
#else:
#    print(f"{username} saved as username!!")

#string indexing [start:end:step]
#DOB = "12-03-04"
#date = DOB[:2]
#print(date)
#month = DOB[3:5]
#print(month)
#year = DOB[7:]
#print(year)
#reverse_DOB = DOB[::-1]
#print(reverse_DOB)

#format specifier

#price1 = 3.15674
#price2 = -5487.111111
#price3 = 20202.1235
#print(f"price = {price1:.1f}")                  #.1f ya .2f se round off hota h
#print(f"price = {price2:020}")                   #:10 matlab 10 space vaala output usi tarah :010 se empty space me 0 aa jaega
#                                                #aise hee :> :< :^ :+ :=
#print(f"price = {price3:+,.2f}")                    #:, se , aa jaega 
#                                                    #do teen need ke hisaab se daal bhi sakte h

#while loop

#name = input("ENTER YOUR NAME : ")
#while name == "":
#    print("INVALID INPUT")
#    name = input("ENTER YOUR NAME : ")
#print(f"hello {name}")

#Compound interest calculator
#principle = float(input("ENTER PRINCIPLE :"))
#while  principle < 0:
#    print("ENTER +VE VALUE")
#    principle = float(input("ENTER PRINCIPLE :"))
#
#rate = float(input("ENTER rate :"))
#while  rate < 0:
#    print("ENTER +VE VALUE")
#    rate = float(input("ENTER rate :"))
#
#
#time = float(input("ENTER time :"))
#while  time < 0:
#    print("ENTER +VE VALUE")
#    time = float(input("ENTER time :"))
#
#total = principle * pow((1+rate/100),time)
#print(f"{total:.2f}")

#FOR loop
#using range 

#for x in range(1,11):       #1 se 10 tak print krega
#    print(x)
#for x in range(1,11,2):     #1 se 10 tak but number skip krke har 2 number i.e 1 3 5 7 9
#    print(x)
#for x in reversed(range(1,11)):         #ulta print krta h
#    print(x)

#phone_no = "1234-5678-90"
#for x in phone_no:
#    print(x)

#for x in range(1,31): 
#    if x % 5 == 0:
#        continue
#    else:
#        print(x)
#
#for x in range(1,31): 
#    if x % 5 == 0:
#        break
#    else:
#        print(x)

#time countdown

#import time
#my_time = int(input("ENTER TIME IN SECONDS : "))
#for x in reversed(range(1,my_time+1)):
#    print(x)
#    time.sleep(1)
#
#print("HIIIII")

#nested loop

#rows = int(input("Enter number of rows: "))
#columns = int(input("Enter number of columns: "))
#symbol = input("Enter symbol to print: ")
#for x in range(rows):
#    for y in range(columns):
#        print(symbol,end=" ")
#    print()

# collections - list,tupple,set
#LISTS - ORDERED AND UNCHANGABLE
#fruits = ["apple","mango","banana"]
#print(help(fruits))                             #VERY IMPORTANT AGAR ISKE OBJECTS BHOOL GAYA TO

#SET - UNORDERED AND IMMUTABLE
#fruits = {"apple","mango","banana","cherry"}
#print(fruits)
#print(help(fruits))                             #VERY IMPORTANT AGAR ISKE OBJECTS BHOOL GAYA TO


#TUPPLE - ORDERED AND CHANGABLE
#fruits = ()"apple","mango","banana")
#print(help(fruits))                             #VERY IMPORTANT AGAR ISKE OBJECTS BHOOL GAYA TO

#2d list
#fast_food = [["burger","pizza","maagi"],
#["apple","mango","banana"],["sprite","pepsi","coke"]]
#
#for x in fast_food:
#    for y in x:
#        print(y,end=" ")
#    print()

#2d numpad dialer printer
#num_pad = [[1,2,3],[4,5,6],[7,8,9],["#",0,"*"]]
#for x in num_pad:
#    for y in x:
#        print(y, end=" ")
#    print()

#import random
#x = int(input("ENTER LOWERBOUND : "))
#y = int(input("ENTER UPPERBOUND : "))
#z = int(input("ENTER YOUR GUESS: "))
#number = random.randint(x,y)
#if number == z:
#    print("CORRECT GUESS")
#else:
#    print("INCORRECT,TRY AGAIN!") 

#function
#def happyBirthday(name,age):
#    print(f"HAPPY BIRTYDAY TO {name}!")
#    print(f"U ARE {age} YEARS OLD!")
#    print("MAY GOD BLESS YOU")
#happyBirthday("NAMAN",21)

#import time
#def count(start,end):
#    for x in range(start,end):
#        print(x)
#        time.sleep(1)
#    print("TIME UP")
#count(1,5)

#iterables
#grades = {"NAMAN" : "A","PARTH" : "B","VIBHANSHU":"C","PRAGATI":"D"}
#student = input("ENTER NAME OF STUDENT:")
#if student in grades:
#    print(f"{student}'s GRADE IS {grades[student]} ")
#else:
#    print(f"{student} WAS NOT FOUND ")'

#MATCH CASE(switch)
#def day_of_week(day):
#    match day:
#        case 1:
#            return "MONDAY"
#        case 2:
#            return "TUESDAY"
#        case 3:
#            return "WEDNESDAY"
#        case 4:
#            return "THRUSDAY"
#        case 5:
#            return "FRIDAY"
#        case 6:
#            return "SATURDAY"
#        case 7:
#            return "SUNDAY"
#        case _:
#            return "INVALID CHOICE"
#print(day_of_week(5))
#def is_weekend(day):
#    match day:
#        case "SATURDAY"|"SUNDAY":
#            return True
#        case "MONDAY"|"TUESDAY"|"WEDNUSDAY"|"THRUSDAY"|"FRIDAY":
#            return False
#        case _:
#            return "INVALID"
#print(is_weekend("MONDAY"))

#module (doosri se import kr sakte h)
#import moduleExample
#result = moduleExample.pi
#print(result)

#OOPs
#class student:
#    def __init__(self,name, section, rollno,is_studying):
#        self.name = name
#        self.section = section
#        self.rollno = rollno
#        self.is_studying = is_studying
#    def topper(self):
#        print(f"SCORES GOOD MARKS AND STUDIES in {stu1.section}")
#    def avg(self):
#        print("SCORES AVERAGE MARKS")
#stu1=student("RAM","A",29,True)
#print(stu1.name)
#print(stu1.section)
#print(stu1.rollno)
#print(stu1.is_studying)
#stu1.topper()

#class Car:
#    colour = "BLACK"    #class variable
#    def __init__(self,model,year,country):
#        self.model = model
#        self.year = year
#        self.country = country
#car1 = Car("TATA CURVE",2024,"INDIA")
#car2 = Car("FERRARI",2022,"ITALY")
#print(car2.model)
#print(car2.year)
#print(car2.country)
#print(Car.colour) #u can call class variable by instance/object name as well as class name

#class animals:
#    def __init__(self,name):
#        self.name=name
#        self.is_healthy = True
#    def eat(self):
#        print(f"{self.name} is eating")
#    def sleep(self):
#        print(f"{self.name} is sleeping")
#class Dog(animals):
#    def speak(self):
#        print("WOOF!")
#class Cat(animals):
#    def speak(self):
#        print("MEOW!")
#Dog1 = Dog("TOMMY")
#Cat1 = Cat("KITTY")
#Dog1.speak()

#from abc import ABC,abstractmethod
#class Shape:
#    def area(self):
#        pass
#class circle(Shape):
#    def __init__(self,radius):
#        self.radius = radius
#    def area(self):
#        return 3.14 * self.radius**2
#class square(Shape):
#    def __init__(self,side):
#        self.side = side
#    def area(self):
#        return self.side**2
#shapes = [circle(2),square(2)]
#for shape in shapes:
#    print(shape.area())

#txt_data = "THIS IS EXAMPLE OF FILE MANAGEMENT"
#file_path="WRITE.txt"
#with open(file_path,"w") as file:
#    file.write(txt_data)
#import datetime
#date = datetime.date(2025,2,1)
#today=datetime.date.today()
#print(today)
#time=datetime.time(10,20,30)
#now = datetime.datetime.now()
#print(now)