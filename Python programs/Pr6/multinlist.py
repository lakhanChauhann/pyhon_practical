a=[]
size=int(input("No of elements"))
for i in range(size):
    val=int(input("Enter number"))
    a.append(val)
mul=1
for i in range(size):
    mul=mul*a[i]
print("Multiplication of all elements in list is",mul)
