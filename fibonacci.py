n=int(input("enter the number: "))
a=0
b=1
c=0
while(c<=n):
    c=a+b
    a=b
    b=c
    print(c)
    print(c,end="\n")