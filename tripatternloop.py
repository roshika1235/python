n=int(input("enter a number"))
k=n
for i in range(0,n):
    for j in range(0,i+1):
        print(k,end="\n")
        k=k-1
    