set1=set(input("Enter set1 values:"))
set2=set(input("Enter set2 values:"))
print("Intersection of set is:",set1.intersection(set2))
print("Union of set is:",set1.union(set2))
print("Differance of set is:",set1.difference(set2))
print("Symmetric Differance of set is:",set1.symmetric_difference(set2))
set1.clear()
print("Set one is cleared",set1)

