colors=["blue","green","red"]
colors.append("purple")
print(colors)
#check
if "lue" in colors:
    print("true")
else:
    print("False")
#sort
colors.sort()
print(colors)
#convert list into string
colors_as_string=repr(colors)
print(colors_as_string)
#join
print("/".join(colors))
#index operator
str="python is good subject"
print(str[0:6:2])
#backward 
print(str[::-1])
