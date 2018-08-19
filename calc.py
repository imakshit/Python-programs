def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Sub")
print("3.Mult.")
print("4.Divide")



num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
choice = input("Enter choice:")

if choice=='1':
    print(add(num1,num2))

if choice=='2':
    print(sub(num1,num2))

if choice=='3':
    print(mult(num1,num2))

if choice=='4':
    print(div(num1,num2))


