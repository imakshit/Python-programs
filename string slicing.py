#input email

email = input("Enter your email id... ")
 #example - adam998@gmail.com
#slice the name

username = email[:email.index('@'):]
domain = email[email.index('@')+1: email.index('.') : ]

#print info of user

print("hey your name is {0} and your email domain is {1}".format(username , domain))
