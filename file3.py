print("Enter the Name of Third File: ", end="")
fileThree = input()

content = ""
f = open("fin.txt", "r")
for line in f:
    content = content + line + '\n'
f.close()

f1 = open("fessay.txt", "r")
for line in f1:
    content = content + line + '\n'
f1.close()

f2 = open(fileThree, "w")
f2.write(content)

print("\nFile merged successfully!") 
