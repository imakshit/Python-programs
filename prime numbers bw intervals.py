lower = int(input("Enter lower interval :"))
upper = int(input("Enter upper interval :"))


print("Prime numbers between" , lower , "and" , upper , "are :")

for num in range(lower , upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
