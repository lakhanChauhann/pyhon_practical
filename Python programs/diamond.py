in[43]:
for i in range (n):
    for j in range(n-i-1):
        print("",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

for i in range (n-1):
    for k in range(i+1):
        print("",end="")
    for j in range(2*(n-i-1)):
        print("*",end="")
    print()
