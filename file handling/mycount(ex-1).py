f=open("file1.txt","r")
temp=f.read()
characters=len(temp)
word=temp.split()
line=temp.split('\n')
print(len(line))
print(len(word))
print(characters)

f.close()
