num = int(input("Enter a number: "))
fact = 1
if num<0:
    print("factorial does not exist...")

elif num==0:
    print("factorial of 0 is 1")

else:
    for i in range(1,num+1):
        fact = fact*i
    print("factorial of number is" , fact)
        
