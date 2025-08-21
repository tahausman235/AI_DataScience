# Q:1
def Greetings(name):
    print("Welcome to SMIT training center,",name)

Greetings("Ahsan")

# Q:2
def number(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"

Number = number(-5)
print(Number)

# Q:3

def large(a,b):
    if a>b:
        print(f"{a} is larger than {b}")
    else:
        print(f"{b} is larger than {a}")

large(5,2)

# Q:4

def larger(a,b,c):
    if a >= b and a >= c:
        print(f"{a} is the largest")
    elif b >= a and b >= c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")

larger(5,2,7)

# Q:5

def age(age):
    if age < 18:
        return "Minor age"
    elif age > 18 and age < 60:
        return "Adult age"
    else:
        return "Senior Citizen"

user_age = int(input("Enter age: "))
aged = age(user_age)
print(aged)

# Q:6

def check(number):
    if number%2==0:
        print("It is even")
    else:
        print("It is odd")

check(5)

# Q:7

def square(num):
    return num**2

user_num = int(input("Enter No which you want to square: "))
sq = square(user_num)
print(sq)

# Q:8

def myRad(r):
    area = 3.14 * r**2
    circum = 2 * 3.14 * r
    return area, circum

area, circumference = myRad(5)
print(f"Area: {area}, Circumference: {circumference:.2f}")

# Q:9

def score(grade):
    if grade>=60:
        print("Pass")
    else:
        print("Fail")

user_score = int(input("Enter Score: "))
score(user_score)

# Q:10

def prime(num):
    if num <= 1:
        print("Not prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not prime number")
            return
    print("Prime number")

prime(5)

# Q:11

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

user_num = int(input("Enter a number: "))
print(f"Factorial of {user_num} is {fact(user_num)}")
    






















    
