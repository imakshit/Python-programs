nterms = int(input("enter the number of terms : "))
n1 = 0
n2 = 1
count = 0

if nterms <=0:
    print("Please enter a positive number")
elif nterms ==1 :
    print("fibonacci series upto 1 terms is : 0")
else:
    print("fibonacci series upto",nterms,"is : ")
    while count<nterms:
        print(n1 , end=" , ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1
