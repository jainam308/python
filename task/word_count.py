a=input("Enter the file you want to count no of words and average no of word length:")
f=open(a,"r")
content=f.read()
s=content.split(".")
words=content.split(" ")
if(s[len(s)-1]==" "):
    average_sentences_length=len(words) /len (s)-1
    print(average_sentences_length,words)
else:
    average_sentences_length=len(words) /len (s)
    print(average_sentences_length,words)








