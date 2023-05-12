n=input("enter the string")
print(n.lower())
print(n.upper())
a="hello i am roshika"           #string index
print(a[1])
b="swetha"
print(len(b))      #length of string
c="check the word from the string "
print("word" in c)                         #finding a word from string
d="hello welcome to python tuturiol"       #split the string"
print(d.split())
e="we are at home"
x=e.split("#")     #spliting using a special character
print(x)
f="THE WORLD IS FULL OF POLLUTION"
y=f.swapcase()                         #swapping uppercase to lowercase
print(y)
g="i like fruits"
z=g.replace("fruits","vegetable")
print(z)                               #replacing a string
h="i need to watch animes"
print(h[4:5])
print(h[5:])              #slicing operations 
print(h[:6])            
print(h[::-1])
k="u and"
k1=" i"                  #concating of string
k2=k+k1
print(k2)

