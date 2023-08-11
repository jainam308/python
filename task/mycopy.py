#program for copy text from one file to another file  
a=input("Enter the file name from you want to read:")
b=input("Enter the file name where you want to copy")
f=open(a,"r")
f1=open(b,"a")
for r in f:
    f1.write(r)
f.close()
f1.close()
print("file are copied")