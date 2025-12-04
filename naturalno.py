# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     {
#         print(i)
#     }

# n = [40, 50, 60, 70, 80]
# for i in n:
#         print(i)


# for str in "DOG":
#     print(str)

# n="ANGEL SINI"
# for i in n:
#     if i =='A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
        # print(i)

# n = "Raspberry"
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i])

# n = ["Dog", "Ostrich", "Eagle", "Penguin", "Butterfly"]
# for i in n:
#     if len(i) >= 7:
#         print(i)

# n = "Butterfly"
# for i in n:
#     print(i)

# # for i in "Butterfly":
# #     if i in "AEIOUaeiou":
# #         print(i)

# n = [4, 6, 10, 15]
# for i in n:
#     print(i**3)

# n = "You look Handsome"
# count = 0
# for i in n:
#     if i in "AEIOUaeiou":
#         count+=1
# print(count)


# n = ["Dog", "Penguin", "Eagle"]
# for i in range(0, len(n)):
#     print("Index",i,"has the word",n[i])

# n = ["Tulip", "Rose", "Lily", "Daisy", "Lotus"]
# for index, value in enumerate(n):
#     print(index, value)     

# n = 8
# for i in range(1, 11):
#     print(i,"*",n,"=",i*n)

# n = {"Maths":90, "Science":90, "Social":90}
# for i,j in n.items():
#     print(i, "=", j)

# n = ["Aeroplane", "Bus", "Helicopter", "Train"]
# for i in n:
#     if i.startswith('A'):
#         print(i)

# n = ((1, 5), (10, 15), (2, 6), (9, 10), (11, 14))
# for i,j in n:
#         print("First",i, "Second",j)

# n = {"Apple", "Orange", "Banana"}
# for i in n:
#     print(i,len(i))

# i=1
# while(i<11):
#     print(i)
#     if(i==5):
#         break
#     i+=1

# n=[1,3,4,6,-3,8,10,-2,-5,2]
# for i in n:
#     if i<0:
#         break
#     print(i)

# n=int(input("Enter a number:"))
# i=1
# while(i<11):
#     print(i)
#     if(i==n):
#         break
#     i+=1

# i=0
# while(i<10):
#     i+=1
#     if(i==5):
#         continue
#     print(i)

# n=[2,3,6,-2,-5,-6,8,10]
# for i in n:
#     if i<0:
#         continue
#     print(i)

# n="Helicopter"
# for i in n:
#     if i not in "AEIOUaeiou":
#         continue
#     print(i)

# for i in range(1,21):
#     if i%3!=0:
#         continue
#     if i==15:
#         break
#     print(i) 

# def first(*a):
#     total=sum(a)
#     print("The sum is",total)
# first(2,3,4,5,6)

# def firstt(**a):
#     for i,j in a.items():
#         print(i,"=",j)
# firstt(Name = "Alice", Age = 25, Place = "Chennai")

# def firsttt(**a):
#     for i,j in a.items():
#         if j>90:
#             print(i)
# firsttt(Alice=90, Vicky=98, Sini=100)
    
# def firstttt(*m):
#     i=1
#     for j in m:
#         i=j*i
#     print(i)
# firstttt(2,3,4)

# def student(*sub, **score):
#     for i,j in score.items():
#         print(i, "=", j)
#     print(sub)
# student("Maths", "Science", "Social", Alice=90, Vicky=98, Sini=100)

# def student(*sub, **score):
#     print(sub)
#     sum=0
#     for i,j in score.items():
#         sum=sum+j
#     print(f"Average Score is: {sum/len(score)}")
# student("Maths", "Science", "Social", Alice = 90, Vicky = 98, Sini = 100)

# cube=lambda x:x**3
# print(cube(5))

# remainder=lambda x,y:x%y
# print(remainder(100,9))

# message=lambda:"Hello!"
# print(message())

# n=[1,2,3,4,5]
# product=map(lambda x:x*2, n)
# print(list(product))

# n=["Apple", "Mango", "Banana", "Orange"]
# string=map(str.upper,n)
# print(list(string))

# n1=[1,2,3]
# n2=[4,5,6]
# add=map(lambda x,y:x+y, n1, n2)
# print(list(add))

# n = [0, 35, 40, 32, 45]
# temp=map(lambda x:x*(9/5)+32, n)
# print(list(temp))

# n = ['Alice', 'Vicky', 'Lolita', 'Nick']
# string=map(len,n)
# print(list(string))

# try:
#     n1 = int(input("Enter first number:"))
#     n2 = int(input("Enter second number:"))
#     div = n1/n2
#     print("The result is:", div)
# except ZeroDivisionError:
#     print("No number can be divided by zero")
# finally:
#     print("Thank you!")

# try:
#     n1 = int(input("Enter first number:"))
#     n2 = int(input("Enter second number:"))
#     div=n1/n2
#     print(f"The result is:{div}")
# except ValueError:
#     print("Invalid input. Please enter a valid number!")
# finally:
#     print("Thank you!")

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     div=n1/n2
#     print(f"The result is:{div}")
# except ZeroDivisionError:
#     print("No number is divisible by zero")
# except ValueError:
#     print("Invalid input. Enter a valid number!")
# finally:
#     print("Thank you!")
    
# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     str=input("Enter a string:")
#     if str=="+":
#         result=n1+n2
#         print("The Addition of two numbers is:", result)
#     elif str=="-":
#         result=n1-n2
#         print("The difference of two numbers is:", result)
#     elif str=="*":
#         result=n1*n2
#         print("The product of two numbers is:", result)
#     elif str=="/":
#         result=n1/n2
#         print("The quotient of two numbers is:",result)
#     elif str=="%":
#         result=n1%n2
#         print("The remainder of two numbers is:",result)
# except ZeroDivisionError:
#     print("No number is divisble by zero!")
# except ValueError:
#     print("Invalid input. Enter a valid number!")
# except IndexError:
#     print("The given index value does not exist!")
# except NameError:
#     print("No such variable is declared!")
# else:
#     print("Sucessfully done")
# finally:
#     print("Thank you!")

# n=[1,2,3,4,5]
# def sum(x):
#     return x+5
# add=map(sum,n)
# print(list(add))

# n=["Apple", "Mango", "Orange"]
# def string(x):
#         return x[0]
# result=map(string,n)
# print(list(result))

# with open("new.txt", "r")as file:
# #     file.write("The weather was cloudy\n")
# #     file.write("But there were no signs of rain today\n")
# #     file.write("Power failure occured frequently at night")
#       count=file.readlines().strip() 
#       print(len(count))

# with open("new.txt", "r")as file:
#     n=[a.strip() for a in file]
#     print(n)

# with open("new.txt","w")as file:
#     x=["Apple","Mango","Cherry"]
#     for i in x:
#         file.write(i+"\n")

# with open("new.txt","r")as file:
#     with open("backup.txt","w")as file1:
#         for x in file:
#             file1.write(x)

# with open("new.txt","r")as file:
#     count=0
#     count=len(x)
#     print(count)

# with open("new1.txt","r")as file:
# #     file.write("Angel,90\n")
# #     file.write("Sini,95\n")
# #     file.write("AngelSini,100")
#       for x in file:
#             n=x.strip().split(",")[0]
#             print(n)

# with open("new2.txt","r")as file:
# #     file.write("Angel,18,Chennai\n")
# #     file.write("Sini,19,Madurai\n")
# #     file.write("AngelSini,20,Kk")
#       n=[]
#       m=[]
#       l=[]
#       for x in file:
#             a=x.strip().split(",")
#             n.append(a[0])
#             m.append(a[1])
#             l.append(a[2])
#       print(n)
#       print(m)
#       print(l)
# with open("new.txt","r")as file:
# # #     file.write("Apple is red in color\n")
# # #     file.write("Apple a day keeps doctor away\n")
# # #     file.write("Orange is tasty\n")
# # #     file.write("Grapes is green in color")
#       words=0
#       for x in file:
#             n=x.strip().split()
#             m=len(n)
#             words+=m
#       print(words)

# with open("new.txt","r")as file:
#     l=[]
#     for x in file:
#         l.extend(x.strip().split())
#     print(l)

# with open("new1.txt","r")as file:
#     m=[]
#     n=[]
#     for x in file:
#         a=x.strip().split(",")
#         m.append(a[0])
#         n.append(a[1])
#     print(m)
#     print(n)

# with open("new1.txt","r")as file:
#     m=[]
#     n=[]
#     for x in file:
#         a=x.strip().split(",")
#         m.append(a[0])
#         n.append(int(a[1]))
#     l=sum(n)
#     print("The total marks is:",l)
#     p=max(n)
#     q=n.index(p)
#     print(m[q],"-",p)  


# with open("new1.txt","r")as file:  
#     m=[]
#     for x in file:
#         a=x.strip().split(",")
#         if int(a[1])>90:
#             m.append(a[0])
#     print(m)
        
# with open("new3.txt","w")as file:
#     for x in m:
#         file.write(f"{x}\n")
# print(len(m))

# n=int(input("Enter a number:"))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# n=input("Enter a string:")
# print(n[::-1])

# n=input("Enter a word:")
# for i in n:
#     if i in "AEIOUaeiou":
#         print(i)

# n=[1,3,5,"Apple",5,"Orange","Apple"]
# m=set(n)
# print(list(m))

# n=[1,2,3,4,5]
# a=map(lambda x:x**2,n)
# print(list(a))

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     div=n1/n2
#     print(div)
# except ZeroDivisionError:
#     print("No number is divisible by zero")
# finally:
#     print("Thank you!")

# with open("neww.txt","r")as file:
# #     file.write("Embedded Design and Development\n")
# #     file.write("Software Development\n")
# #     file.write("Mobile Apps Development")
#       print(file.read())

# def largest(*n):
#     print(max(n))
# largest(5,6,7,8,9)

# age=int(input("Enter your age:"))       
# assert age>18,  "Must be greater than 18"
# print("Eligible")

# n1={"Angel":90, "Sini":95, "AngelSini":100}
# n2={"Kavin":96, "Angel":98, "KavinJudeSnowin":100}
# n3={"Angel":100,"Kavinn":90, "Sinii":92}
# n4={**n1,**n2,**n3}
# print(n4)


# class laptop:
#     def __init__(self,brand,ramsize):
#         self.brand_name=brand
#         self.ram_size=ramsize
#     def specs(self):
#         print("Laptop Brand:",self.brand_name,",","Ram size=",self.ram_size)
# l1=laptop("Dell",64)
# l2=laptop("Asus Vivobook",64)
# l1.specs()
# l2.specs()

# class Animals:
#     def __init__(self,type,color,feature):
#         self.animal_type=type
#         self.animal_color=color
#         self.animal_feature=feature
#     def use(self):
#         print(f"{self.animal_type} is {self.animal_color} in color and has {self.animal_feature}")
# a1=Animals("Dog","Brown","Paws")
# a2=Animals("Cat","White","Whiskers")
# a1.use()
# a2.use()

# class Vehicles:
#     def __init__(self):
#         print("Used for transportation")
# class car(Vehicles):
#     def opentrunk(self):
#         print("Driving")
# class bike(Vehicles):
#     def kickstart(self):
#         print("Riding")
# v1=car()
# v2=bike()
# v1.opentrunk()
# v2.kickstart()

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i)

# n=int(input("Enter a number:"))
# if n%2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")

# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# n3=int(input("Enter third numnber:"))
# if(n1>n2 and n1>n3):
#     print("The largest number is",n1)
# elif(n2>n1 and n2>n3):
#     print("The largest number is",n2)
# else:
#     print("The largest number is",n3)

# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n="MANGO"
# rev=""
# for i in n:
#     rev=i+rev
# print(rev)

# # n=int(input("Enter a number:"))
# # for i in range(1,11):
# #     m=n*i
# #     print(m)

# str=input()
# vowel=0
# cons=0
# for i in str:
#     if i.isalpha():
#         if i in "AEIOUaeiou":
#             vowel+=1
#         else:
#             cons+=1
# print("The vowels in the given string are:",vowel)
# print("The consonants in the given string are:",cons)

# n=int(input("Enter a number:"))
# if n<=1:
#     print("Not a prime number")
# else:
#        for i in range(2,n):
#            if n%i==0:
#                 print("Not a Prime Number")
#                 break
#        else:
#            print("Prime number")

# N=[1,2,3,5,9]
# m=sum(N)
# print(m)

# a=0
# b=1
# n=int(input("Enter terms:"))
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# marks=int(input("Enter the mark:"))
# if(marks>90):
#     print("A")
# elif(marks>80):
#     print("B")
# elif(marks>70):
#     print("C")
# else:
#     print("fail")
# i=1
# while(i<=15):
#     print(i , end= " ")
#     i+=1
    
    
# n=int(input("Enter the size"))
# m=[]
# for i in range(n):
#         l=int(input())
#         m.append(l)
# for i in m:
#     print(i , end = " ")
    
# for i in range(1,10,3):
#     print(i)

# x=5
# y=5
# print(x==y ,  "," , x is y)

# count=0
# vowel="AEIOUaeiou"
# str=input("Enter a string:");
# for i in str:
#         if i in vowel:
#                 count+=1
# print(count)

# fact=1
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     fact=fact*i
#     i+=1
# print(fact)

# str=input("Enter a string:")
# chr=input("Enter a character:")
# if chr in str:
#     print("Present")
# else:
#     print("Not Present")
    


# str=input("Enter a string:")                                   
# ch1=input("Enter a character:")
# ch2=input("Enter a character:")
# str1=" "
# for i in str.lower():
#     if ch1==i:                       
#         str1=str1+ch2
#     else:
#         str1=str1+i
# print(str1)                           
        
 
# str1=input("Enter a String:")
# str2=input("Enter a String:")
# if sorted(str1.lower())==sorted(str2.lower()):
#     print("Anagram")
# else:
#     print("Not an Anagram")

# n=int(input("Enter the number of elements:"))
# arr=[]
# for i in range(n):
#     m=int(input())
#     arr.append(m)
# arr.sort()
# print(arr[-2])

# str=input("Enter a string:")
# str1=" "
# for i in str:
#     if ord(i)>=97 and ord(i)<=122:
#         str1=str1+chr((ord(i)-32))
#     else:
#         str1=str1+i

# n=int(input("Enter a number"))
# a=True
# for i in range(1,n+1):
#     if(n%i==0):
#         if(a==False):
#             print("," , end = "")
#         print(i, end = "")   
#         a=False


# n=(2,6,8,12,4,11,7,15,19,20)
# m=n[2:8]
# print(m)


# def product(m):
#     print(m*m)
# product(m=6)
        

# def number(m="Hey"):
#     print(m, "Hello")
# number("Hello")

# def number(*score):
#     sum=0
#     for i in score:
#         sum=sum+i
#     print(sum)
# number(90,85,70,90,87)

# def number(**score):
#     for i,j in score.items():
#         print(i, "=", j)
# number(Name="Angel", Age = 21, Hobby = "Gardening")

# l=[]
# n=int(input("Enter the size:"))
# for i in range(n):
#     m=int(input())
#     l.append(m)
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)

# l=[]
# n=int(input("Enter the size:"))
# for i in range(n):
#     m=int(input())
#     l.append(m)
# for i in l:
#     s=i*i
#     print(s)

# s=input("Enter a string:")
# print(s[::-1])

# def product(x,y,z):
#     return x*y*z
# set1=[1,2,4]
# set2=[2,3,4]
# set3=[3,4,5]
# result=map(lambda x,y,z:x*y*z,set1,set2,set3)
# print(list(result))

# n=map(int,input("Enter the numbers:").split(","))
# print(set(n))

# age=int(input("Enter the age:"))
# assert age>18, "Age not greater than 18"
# print("Age greater than 18")

# n=input("Enter a string:")
# print("Even indexes:", n[0::2])

# l=[]
# n=int(input("Enter the size:"))
# for i in range(n):
#     m=int(input())
#     l.append(m)
# a=int(input("Enter a number:"))
# flag=0
# for i in l:
#      if (a==i):
#         flag=1
#         break    
# if flag == 1:
#      print("found")     
# else:
#      print("Element is not present in the list")
# if a in l:
#     print("found")
# else:
#     print("not found")

# str1=input("Enter a String:")
# str2=""
# for i in str1:
#     if i in "AEIOUaeiou":
#         str2=str2 + "*"
#     else:
#         str2=str2 + i
# print(str2)

# n1=list(map(int,input("Enter the numbers:").split(",")))
# assert len(n1)>0, "List is empty"
# print("List is not empty", sum(n1))

# d={"Name":"Angel","Age":21,"Hobby":"Gardening"}
# print(d["Name"])
# print(d["Age"])
# print(d.get("Degree", "Key not found"))


# s=input("Enter a String:")
# t=s[::-1]
# if t==s:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# count=0
# l=list(map(int,input("Enter the marks:").split(",")))
# n=sum(l)/len(l)
# for i in l:
#     if i>n:
#         count+=1
# print(count)
    
# t=tuple(map(int,input("Enter the numbers:").split(",")))
# s=t[::-1]
# print(s)
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# def student(**n):
#     for i,j in n.items():
#         print(i,"=", j)
# student(a="Angel Sini",b=21)

# n=map(int,input("Enter the elements:").split(","))
# l=[]
# for i in n:
#     if i not in l:   
#         l.append(i)    
# print(l)

# l=[]
# n=map(int,input("Enter the elements:").split(","))
# m=int(input())
# for i in range(len(n)):
#     if n[i]==m

# def numbers(*n):
#     prod=1
#     for i in n:
#         prod=prod*i
#     print(prod)
# numbers(6,7,9,12)

# n=[2,4,9,8,4,10]
# n.sort()
# m=int(input("Enter the element:"))
# left=0
# right=len(n)-1
# found=False
# while left<=right:
#     mid=(left+right)//2
#     if n[mid]==m:
#         found=True
#         break
#     elif n[mid]<=m:
#         left=mid+1
#     else:
#         right=mid-1
# if not found:
#     print("The value is not found")
# else:
#     print("The value is found")

# n=[2,4,9,8,4,10]
# m=int(input("Enter the element:"))
# found=False
# for i in range(len(n)):
#     if n[i]==m:
#         found=True
# if not found:
#         print("The element is not found")
# else:
#         print("The element is found")

# s=input("Enter a String:")
# r=s[::-1]
# if r==s:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# s=input("Enter a String:")
# count=0
# for i in s:
#     if i in "AEIOUaeiou":
#         count+=1
# print(count)

# n=int(input("Enter a number:"))
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")   0 1 1 2 3 5
#     c=a+b 0+1=1 1+1=2   1+2=3  2+3=5  3+5=8
#     a=b   1     1       2      3      5
#     b=c   1     2       3      5      8

# "5678"
# n=input("Enter a string")
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(sum)

    
# fact=1
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("Factorial is:",fact)

# s=input("Enter a String:")   
# t={}                         
# for i in s:                  
#     t[i]=t.get(i,0)+1        
# for a,b in t.items():
#     print(a, "-", b)


# arr=[]
# n=int(input("Enter the array size:"))
# for i in range(n):
#     m=int(input())
#     arr.append(m)
# big=max(arr)
# print(big)

# n=int(input("Enter a number:"))
# for i in range(2,n+1):    2 3 4 5 6 7 8 9
#     prime=True             
#     for j in range(2,i):  2,2 2,3 2,4 2,5 2,6 2,7 2,8 2,9
#         if i%j==0:         
#             prime=False
#             break
#     if prime:
#         print(i)         2 3 5 7 

# n=input("Enter a String:")
# m=n.replace(" ", "")
# print(m)

# arr=[]
# n=int(input("Enter the array size:"))
# for i in range(n):
#     m=int(input())
#     arr.append(m)
# arr1=set(arr)
# arr2=list(arr1)
# arr2.sort()
# print(arr2[-2])

# arr=[]
# arr1=[]
# n=int(input("Enter the array size:"))
# for i in range(n):
#     m=int(input())
#     arr.append(m)
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print(arr1)

# arr=[]
# n=int(input("Enter the array size:"))   
# for i in range(n):
#     m=int(input())
#     arr.append(m)
# for i in range(len(arr)):                  0 1 2
#     for j in range(i+1, len(arr)):         1 2 3   2 3  3
#         if arr[i]>arr[j]:                  
#             temp=arr[i]                     25  32  90
#             arr[i]=arr[j]                   22  25  32
#             arr[j]=temp                     25  32  90
# print(arr)
            
# arr1=list(map(int,input("Enter the size:").split(",")))
# arr2=list(map(int,input("Enter the size:").split(",")))
# arr3=arr1+arr2
# print(arr3)

# arr=[1,3,2,5,9,10]
# n=int(input("Enter a number:"))
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]+arr[j]==n:
#             print(arr[i],",",arr[j])

# str1=input("Enter a string:").lower()
# str2=input("Enter another string:").lower()
# str3=sorted(str1)
# str4=sorted(str2)
# if(str3==str4):
#     print("Strings are Anagram")
# else:
#     print("Strings are not an Anagram")

# str=input("Enter a string:")   
# str1=str.split()         
# str2=""  
# for i in str1:
#     if len(i)>len(str2):
#         str2=i
# print(str2)

# str=input("Enter a string:")
# str1=""
# for i in str:
#     if ord(i)>=97 and ord(i)<=122:
#              str1=str1+chr(ord(i)-32)
#     else:
#              str1=str1+i
# print(str1)

# str1=""
# str=input("Enter a string:")
# chr1=input("Enter a character to replace:")
# chr2=input("Enter a character to be replaced:")
# for i in str:
#     if i==chr1:
#         str1=str1+chr2
#     else:
#         str1=str1+i
# print(str1)


# str=input("Enter a String:").split()
# print(str)
# str2=len(str)
# print(str2)


# 123
# 1^3+2^3+3^3=123

# 123
# 1!+2!+3!=123

# remainder=lambda: "Hey Kavin"
# print(remainder())

# remainder=lambda:[2,3,4,5,6]
# print(remainder()[0])

# def sum(x,y):
#     s=x+y
#     return s
#     print(s)
# print(sum(5,6))



        




    

            
 


    



     








    
    

    
    





      



        



        



    
        
        


    






            









        



 


                  



        
          
           




    





    

    








        

  






   
    
        
 



        
       













    


