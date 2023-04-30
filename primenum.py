first=int(input("enter the first digit: "))
end=int(input("enter the ending digit: "))
for i in range(first,end):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")