tup1=("swetha","roshika","sharon","sahithi")
print(tup1)
tup2=("swetha","swetha","roshika","deepu")
print(tup2)
print(len(tup1))
print(type(tup1))
tup3=(1,2,3,"dhoni","True")
print(tup3)
print(tup3[-1])
print(tup3[3])
print(tup3[2:5])
tup2=list(tup1)
tup2[2]=7
tup1=tuple(tup2)
print(tup1)
y=list(tup2)
y.append("sahithi")
tup2=tuple(y)
print(tup2)


