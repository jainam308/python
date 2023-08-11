#program for checking string to palindrome or not
def palindrome(s):
    s1=s[::-1]
    print(s,"=",s1)
    if(s==s1):
        print("palindrome")
    else:
        print("not palindrome")
s=input("enter string :")
palindrome(s)