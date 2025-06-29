def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Cannot divide by zero")
    else:
        return a/b
    
while True:
    ase = input("Enter add,sub,mul,div,q:")
    if ase == "q":
        print("Bye")
        break
    a = float(input("Enter num1:"))
    b = float(input("Enter num2:"))
    if ase == "add":
        print(add(a,b))
    elif ase == "sub":
        print(sub(a,b))
    elif ase == "mul":
        print(mul(a,b))
    elif ase == "div":
        print(div(a,b))
    else:
        print("Enter valid details")