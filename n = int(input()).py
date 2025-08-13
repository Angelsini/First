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



    
    





            









        



 


                  



        
          
           




    





    

    








        

  






   
    
        
 



        
       













    


