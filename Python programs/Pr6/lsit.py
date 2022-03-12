a=[]
size=int(input("No of elements"))
for i in range(size):
    val=int(input("Enter number"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("sum of all elemts in list is",sum)
