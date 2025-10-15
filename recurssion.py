# def print_nums(n):
#     for item in range(1,n+1):
#         print(item)
# print_nums(10)

# start = 1
# def print_nums1(num):
#     global start
#     print(start)
#     start +=1
#     if start<=num:
#         print_nums1(num)

# print_nums1(20)


# def hello(name): #def function 1 parameter
#     print("hi",name)
# hello1 = hello
# hello1("xyz") #this is the argument 1 passing


# def add(a,b):
#     print("addition of two numbers")
#     print(a+b)

# def sub(a,b):
#     print("sub of two numbers")
#     print(a-b)
# def mul(a,b):
#     print("mul of two numbers")
#     print(a*b)

# def div(a,b):
#     print("div of two numbers")
#     print(a/b)
# def square(a,b):
#     print("square of two numbers")
#     print(a*b)
# def mod(a,b):
#     print("mod of two numbers")
#     print(a%b)
# def expontional(a,b):
#     print("expontional of two numbers")
#     print(a**b)

# operation_type = {
#     "add":add,
#     "sub":sub,
#     "mul":mul,
#     "div":div,
#     "square":square,
#     "mod":mod,

# }

# def calulate(a=10,b=20,opty="add"):
#     call_back = operation_type["sub"]
#     call_back(a,b)

# calulate(2,8)




# def addition():
#     a = 10
#     b = 20
#     print(a+b)

# addition()

i = 1
while i <= 10:
    if( i%2 == 0):
        i += 1

print(i)


# a = 10
# b = 20
# print(a/b)

def greet():
    print("Hello from recursion!")

greet()
