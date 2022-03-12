a=[]
b=[]
size=int(input("No of elements"))
print("Enter first list")
for i in range(size):
    val1=int(input("Enter number:"))
    a.append(val1)
    
print("Enter second list")
for i in range(size):
    val2=int(input("Enter number:"))
    b.append(val2)
    
a_set=set(a)
b_set=set(b)

if(a_set & b_set):
    print("Common elemnt in both list is:",a_set & b_set)
else:
    print("There is no common element in both list")

        
