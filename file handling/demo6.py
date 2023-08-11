f=open("file3.txt","a+")
if f:
    print("file opened sucessfully")
f.write("hello world")
t=f.read()
print(t)
f.close()