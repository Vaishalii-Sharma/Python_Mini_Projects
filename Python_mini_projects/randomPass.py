import random
import string

password_length = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(password_length):
    password += random.choice(charValues)

print("your random password is: ",password)


#list comprehension [function for i in range(n)]
#res = [random.choice(charValues) for i in range(password_length)]
#print(res)
