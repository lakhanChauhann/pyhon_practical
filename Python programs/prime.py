m=0
flag=0
i=2
n=input("Enter a number ")
n=int(n)
m=(int(n)/2)
m=int(m)+1
for i in range(m):
    if(n%i==0):
        print("Number is not prime")
        flag=1
        i+=1
        break
if(flag==0):
    print("Number is prime")
