def string_test(s):
    d={"Upper Case":0, "Lower Case":0}
    for c in s:
        if c.isupper():
            d["Upper Case"]+=1
        elif c.islower():
            d["Lower Case"]+=1
        else:
            pass
    print("Number of Upper case characters:",d["Upper Case"])
    print("Number of Lower case characters:",d["Lower Case"])
str=input("Enetr a string: ")
string_test(str)  