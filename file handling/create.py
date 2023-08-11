f=open("file2.txt","x")
print(f)
if f:
    print("file opened sucssessfully")
f.write("helo")
f.close()