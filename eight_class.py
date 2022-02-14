import random
import string
# cal = ()

# def cal(): # Defining a function #
#     print(2+2)
#     return 2+2
# a = cal() # Calling a function #
# print(a)

# def cal(x,y):
#     print(x-y)
# # cal(10,5)
# # cal(y=5,x=10)
# cal(y=10)

# def cal(x,y=5):
#     print(x-y)
# cal(10,2)

# def num(x):
#     return (x % 2 !=0)
# a = num(6)
# print(a)

# def num(n):
#     if n % 2 ==0:
#         return True
#     else:
#         return False
# b = num(3)
# print(b)

# def is_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
    
#     square_root = int(n**0.5)
#     for i in range(2, square_root + 1):
#         if(n % i==0):
#             return False
#         return True
# b = is_prime(9)
# print(b)

# import re

# def validate():
#     while True:
#         password = input("Enter a password: ")
#         if len(password) > 8:
#             print("Make sure your password is less than 8 letters")

#         elif re.search('[0-9]',password) is None:
#             print("Make sure your password has a number in it")

#         elif re.search('[A-Z]',password) is None: 
#             print("Make sure your password has a capital letter in it")

#         elif re.search('[a-z]',password) is None: 
#             print("Make sure your password has a lower letter in it")

#         elif re.search('[!, @, $, #]',password) is None: 
#             print("Make sure your password has at least one special character")

#         else:
#             print("Your password is valid")
#             break

# validate()


# def passwd_check(passwd):
#     isValid = True
#     Special_Char=['$','@','#', '!']

    
#     if len(passwd) < 8:
#         print('the length of password should not be less than 6')
#         isValid = False

#     if not any(char.isdigit() for char in passwd):
#         print('the password should have at least one number')
#         isValid = False

#     if not any(char.isupper() for char in passwd):
#         print('the password should have at least one uppercase letter')
#         isValid = False

#     if not any(char.islower() for char in passwd):
#         print('the password should have at least one lowercase letter')
#         isValid = False
        
#     if not any(char in Special_Char for char in passwd):
#         print('the password should have at least one of the special symbols')
#         isValid = False
#     if isValid:
#         return "Strong Password"
#     else:
#         return "Not strong enough"


# dat = passwd_check("Thimzy")
# print(dat)

print('Hello, Welcome to password generator!')

#Input the lenght of password
length = int(input('Enter the length of password:\n>'))
#Define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#Combine the data
all = lower + upper + num + symbols
#use random
temp = random.sample(all,length)
#Create the password
password = "".join(temp)
print(password)
