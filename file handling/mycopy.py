fr=open("file1.txt","r")
fw=open("file5.txt","a")
for r in fr:
    fw.write(r)
fr.close()
fw.close()
print("copied")