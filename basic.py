# # def greet(name, greeting="Hello"):
# #     return f"{greeting}, {name}!"

# # print(greet("Eve"))

# # print("hello world")

# # # Simple addition program
# # num1 = int(input("Enter first number: "))
# # num2 = int(input("Enter second number: "))

# # sum = num1 + num2
# # print("The sum is:", sum) 

# # for i in [1,2,3,4,5,6,7,8]:
# #     print(i)

# # for i in (1,2,3,4,5,6,7,8):
# #     print(i)

# # for i in "hello":
# #     print(i)
# # for i in range(1,10):
# #     print(i)

# # family = {
# #     "name":"xyz",
# #     "faname":"fa",
# #     "maname":"ma"
# # }

# # for fam in family:
# #     print(fam,family[fam])
# # print(family["name"])
# # print(family.get('ceo','damn'))

# # familylist = [
# #     {
# #         "name":"a",
# #         "faname":"fa",
# #         "maname":"ma",
# #     },

# #     {
# #          "name":"a1",
# #         "faname":"fa1",
# #         "maname":"ma1",
# #     },

# #     {
# #          "name":"a2",
# #         "faname":"fa2",
# #         "maname":"ma2",
# #     }
    
# # ]
# # for flist in familylist:
# #     print(flist["name"])
# #     if flist["name"] =="a":
# #         continue
# #     flist.update({"country":"india"})
# #     print(flist)

# # print(flist,familylist)


# #continue and break

# # vowels = ['a', 'e', 'i', 'o', 'u']
# # countryname ="iandia"

# # for char in countryname:
# #     if char in vowels:
# #         continue
# #     print(char)

# # for char in countryname:
# #     if char  == "a":
# #         break
# #     print(char)



# nums = [1,2,3,4,5,6,7,10,20,30]
# # totalnumber = 0
# # for num in nums:
# #     print(num)
# #     # totalnumber = totalnumber+num
# #     totalnumber += num
# #     print(totalnumber)


# # evennumber =[]
# # oddnumber = []

# # for i in nums:
# #     if i%2 ==0:
# #         print(i,"even")
# #         evennumber.append(i)
# #         print(evennumber)
# #     else:
# #         print(i,"odd")
# #         oddnumber.append(i)
        
# # print(oddnumber,evennumber)


# names = {'a', 'b',  'c', 'd', 'e'} # mutable and set is unorderd & accepts unique valurs
# names.add('z')
# names.remove('d')
# names.discard('s')
# print(names)


# fruits =['apple','mango','apple','mango']
# unique_fruits = (list(set(fruits)))
# print(unique_fruits)

# #function is a block of code whicj gets excuted upon calling its name.
# def logmessage():
#     fruits = ['apple','mango']
#     print(fruits)

# logmessage()

age = 100
salary = 1000.100
name = "abcd"
isValid = True
isAuthor = False
isSupportonlyCSV = True

print(age<=18)
if age <=18:
    print("he is teen")
elif age>=10 and age <=60:
    print("he is adult")
else:
    print("he is too old")


a = 10
b = 20
print(a+b)
