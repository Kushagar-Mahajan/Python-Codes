#this is project of slicing out the email address

#get user email address
email = input("What is your email address?: ").strip()

#slice out user name
user = email[:email.index("@")]

#slice out domain name
domain = email[email.index("@")+1:] #+1 is used as we don't want to add @ in our answer

#format message
output = "Your username is {} and your domain name is {}".format(user, domain)

#display output message
print(output)