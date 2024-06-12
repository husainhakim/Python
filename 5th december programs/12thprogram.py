# usernames=[]
# domains=[]


# for i in range(5):
#       email=input('Enter the email adress:-')
#       if '@' not in email:
#            print("Email adress galat hai bhai")
#            break
#       else:
#        print(email)
#       if '@' in email:
#        username,domain=email.split('@')
#        usernames.append(username)
#        domains.append(domain)
#        email_mytuple=(username,domain)
#        print('User name:-',username)
#        print('Domain:-',domain)
#       print(usernames)
#       print(domains)
email=int(input("Enter number of email"))
for i in range(0,email):
    x=str(input("Enter your email address: ")).split("@")
    s=(x[0])
    d=(x[1])
    print('Username :',s)
    print('Domain :',d)
     