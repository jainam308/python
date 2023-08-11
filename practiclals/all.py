# a=int(input("ENter number"))
# if(a%2==0):
#     print(a,"is even")
# else:
#     print(a,"is odd")    

# marks=20
# if(marks >=80):
#     print("A")
# else:
#     if(marks>=70):
#         print("B")
#     else:
#         if(marks>=40):
#             print("c")
#         else:
#             print("fail")
# num=1
# while num<=5:
#     print(num)
#     num=num+1
# for i in range(1,21,2):
#     print(i)
# for ch in 'python':
#     if(ch=='h'):
#         pass
#     print(ch)
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
# def lis(l):
#     l2=[]
#     for num in l:
#         if num not in l2:
#             l2.append(num)
#     return l2
# l=[1,2,3,4,5,2]
# x=lis(l)
# print(x)
# ----------------------------Exercise ch-5
# def palindrome(s):
#     s1=s[::-1]
#     print(s1)
#     if(s==s1):
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome("jainam")        
# def anagram(n1,n2):
#     if(sorted(n1)==sorted(n2)):
#         print("anagram")
#     else:
#         print("not anagram")
# n1=input("enter word:")
# n2=input("enter another word:")
# anagram(n1,n2)
  
# s=input("enter string:")
# s1=s[::-1]
# print(s1)
l=["jainam",32]
print(l)

# tu=("jainam",1,32,32.6,32)
# print(tu)
# x=set(tu)
# print(x)
# y=list(tu)
# print(y)
# z=str(tu)
# print(type(z))
# del tu
dic={1:"hello",2:"hi"}
for i in dic.items():
    print(i)
print(dic.items())





