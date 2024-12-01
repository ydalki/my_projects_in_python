print("""************************
      
      basic calculator

      ***************************""")

a=int(input("first number:"))
b=int(input("second number:"))

process=input("enter the opeartion:")

if process=="total":
    print(f" a:{a} and b:{b}, total:{a+b}")
elif process=="subtract":
    print(f" a:{a} and b:{b}, subtract:{a-b}")
elif process=="divide":
    print(f" a:{a} and b:{b}, divide:{a/b}")
elif process=="multiply":
    print(f" a:{a} and b:{b}, multiply:{a*b}")
else:
    print("invalid process")    



