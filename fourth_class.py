#......Dictionary.......#
# my_dict = {"key":"This is the value", "key2":"This is another key"}

# # # my_Dict = dict()
# # my_dict ={"key":"This is the new value"}#To change an existing value

# a = {"key7":"This is the value", "key5":"This is another key"}

# my_dict.update(a)#To add to the multiples keys to a dictionary

# # print(my_dict.keys())#To know the number of keys in your dictionary
# # print(my_dict.values())#To know the number of values in your dictionary
# # print(my_dict.items())

# b = [('key', 'This is the new value'), ('key7', 'This is the value'), ('key5', 'This is another key')]

# # print(dict(b))

# # popped = my_dict.pop("key7")
# # print(popped)
# # print(my_dict)

# print(my_dict.get("xyz", "Not found"))


# data = {"name":"chucks","location":"Aba","Job":"Senior Frontend","Salary":"$50,000"}
# data["city"] = data.pop("location")
# print(data)

# .......Conditionals........#
# if "ada" == "john":
#     print("Correct")
# else:
#     print("Incorrect")

# user_data = {"thimzy@gmail.com":"Oloba Thimzy"}

# user_email = input("Enter your email:\n>").lower()

# if user_email.isspace() or user_email == "":
#     print("No entry")
# else:
#     if user_email in user_data.keys():
#         print("Account already exists")
#     else:
#         choice = input("Do you want to subscribe?(Y/y or N/n)\n>").lower()

#         if choice == 'y':
#             name = input("Enter your full name:\n>")
#             user_data[user_email] = name
#             print("successfully subscribed.")

#         elif choice == 'n':
#             print("Goodbye!")
#         else:
#             print("Invalid input")
# print(user_data)


#.......bank app v1....#
import random


data = {
    "3947758457" : {
        "name":"Thimzy",
        "dob": "09-09-09",
        "bvn": "12345678912",
        "pin": "1234",
        "bal": 120000
    },
    "3927758475" : {
        "name":"Samklef",
        "dob": "09-09-79",
        "bvn": "12341678912",
        "pin": "1214",
        "bal" : 15000
    },
}


print("Welcome to the AstroBank App")
print("Enter s to signup or l to login")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("Enter your account num:\n>")
    pin = input("Enter your pin:\n>")

    user = data.get(acc_num)

    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
        print("Enter d to Deposit or w to Withdraw or q to quit:")
        choice_2 = input(">").lower()

        if choice_2 == "d":
            acc_num_1 = input("Enter your account num: \n>")
            pin_1 = input("Enter your pin: \n>")

            user_1 = data.get(acc_num_1)

            if user_1 and user_1['pin'] == pin_1:
                print(f"Welcome {user_1['name']}.\nYour account balance is ${user_1['bal']}")
                dep_amount_1 = input("Enter Deposit amount: \n>") 
                dep_amount_1= int(dep_amount_1)
                user_1["bal"] += dep_amount_1
                print(user_1)
            else:
                print("Invalid Login") 
                print("4 more tries")

        elif choice_2 == "w":  
              acc_num_4 = input("Enter your account num\n>")
              pin_4 = input("Enter your pin:\n>")

              user_4 = data.get(acc_num_4)

              if user_4 and user_4['pin'] == pin_4:
                print(f"Welcome {user_4['name']}.\nYour account balance is ${user_4['bal']}")
                withdrawal_amount = input("Enter Withdrawal amount: \n>") 
                withdrawal_amount = int(withdrawal_amount)
                user_4["bal"] -= withdrawal_amount
                print(user_4)
              else:
                print("Invalid Login") 
                print("4 more tries")
        if choice_2 == "q":  
           print("Goodbye from Astroverse Bank")
    else:
        print("Invalid Login") 
        print("Invalid Login")
# Sign-up or Registration Process Algorithm -#1
elif choice == 's':
    user_name = input("Enter your full name:\n>").lower()
    user_dob = input("Enter your dob mm-dd-yyyy:\n>").lower()
    user_bvn = input("Enter your BVN :\n>").lower()
    # user_bvn = int(user_bvn)
    user_pin = input("Enter your 4 Digit PIN :\n>").lower()
    # user_pin = int(user_pin)

    if type(user_name) == type("String") and type(user_dob) == type("String") and type(user_bvn) == type("String") and len(user_bvn) == 11 and type(user_pin) == type("String") and len(user_pin) == 4:

       acct_data = {}
       acct_data["name"]= user_name
       acct_data["dob"] = user_dob
       acct_data["bvn"] = user_bvn
       acct_data["pin"] = user_pin
       acct_data["bal"] = 0
       user_acct_num = random.randrange(1111111111,9999999999)
       user_acct_num = str(user_acct_num)
       new_acct = {}
       new_acct[user_acct_num] = acct_data
       data.update(new_acct)


       print(f"Congratulations!, {acct_data['name']} You now have an accont on Astroverse Bank App and you account number is \n>")
       print(list(data.keys())[-1])
       print("Enter d to Deposit or q to quit:")
       choice_2 = input(">").lower()

       if choice_2 == "d":
            acc_num_2 = input("Enter your account num: \n>")
            pin_2 = input("Enter your pin: \n>")
            # pin_2 = int(pin_2)
            user_2 = data.get(acc_num_2)

            if user_2 and user_2['pin'] == pin_2:
                print(f"Welcome {user_2['name']}.\nYour account balance is ${user_2['bal']}")
                dep_amount = input("Enter Deposit amount: \n>") 
                dep_amount= int(dep_amount)
                user_2["bal"] += dep_amount

                print(user_2)
                print("Enter w to withdraw q to quit \n>")
                choice_3 = input(">").lower()
                if choice_3 == "w":  
                  acc_num_3 = input("Enter your account num\n>")
                  pin_3 = input("Enter your pin:\n>")
            #   pin_3 = int(pin_3)
                  user_3 = data.get(acc_num_3)

                  if user_3 and user_3['pin'] == pin_3:
                    print(f"Welcome {user_3['name']}.\nYour account balance is ${user_3['bal']}")
                    withdrawal_amount = input("Enter Withdrawal amount: \n>") 
                    withdrawal_amount = int(withdrawal_amount)
                    user_3["bal"] -= withdrawal_amount
                    print(user_3)
                  else:
                        print("Invalid Login") 
                        print("4 more tries")
       elif choice_2 == "q": 
         print("Goodbye from Astroverse Bank")  






else:
        print("Invalid data") 











