dic1={'a':100,'b':200,'c':300}
dic2={'a':400,'d':600,'b':400}
dic3={}
for key in dic2:
    if key in dic1:
        dic3[key]=dic2[key]+dic1[key]
for key in dic2:
    if key not in dic1:
        dic3.add(dic1)
print(dic3)
        
