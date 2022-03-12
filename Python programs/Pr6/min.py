a=[]
size=int(input("No of elements:"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)

print("Smallest number in the list is:",min(a))
