#average
# a=int(input("enter marks:"))
# a1=int(input("enter marks:"))
# a2=int(input("enter marks:"))
# b=(a1+a2+a)/3
# print(b)

#circle and perimeter
# from math import pi
# r=int(input("Enter the radius"))
# a=pi*r**2
# p=2*pi*r
# d=2*r
# print(a)
# print(p)

# even or odd
# n=int(input("enter number:"))
# if(n%2==0):
#     print("number is even")
# else:
#     print("number is odd")

#prime or not prime
# flag=True
# n=int(input("enter number:"))
# if n < 2:
#          flag=False
# else:
#     for i in range(2,n):
#         if(n%i==0):
#             flag=False
#             break
#         flag=True
# if(flag):
#       print("Number is prime")
# else:
#       print("number is not prime")

# def maximum(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# a=int(input("enter number 1:"))
# b=int(input("enter number 2:"))
# c=int(input("enter number 3:"))
# x=maximum(a,b,c)
# print(x,"is greatest")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#mutlipication of table
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

#sum of n elements
# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

#sum of all odd and even num
# n=int(input("enter number:"))
# even_sum=0
# odd_sum=0
# for i in range(1,n):
#     if n%2==0:
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i
# print(even_sum)
# print(odd_sum)

# def palindrome(s):
#     s1=s[::-1]
#     print(s,"=",s1)
#     if(s==s1):
#         print("palindrome")
#     else:
#         print("not palindrome")
# num=123321
# x=str(num)
# palindrome(x)

# str="jainam"
# count=0
# for i in str:
#     count +=1
# print(count)

# l=[10,20,25,30,35]
# l2=[40,45,60,75,90]
# l3=[]
# for i in l:
#     if i%2!=0:
#         l3.append(i)
# for i in l2:
#     if i%2==0:
#         l3.append(i)
# print(l3)

str=["Name","is","James"]
print("**".join(str))



