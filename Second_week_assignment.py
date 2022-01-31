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
        "bvn": "12341678932",
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
                print("Pin not correct") 

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
                print("Pin not correct") 
        if choice_2 == "q":  
           print("Goodbye from Astroverse Bank")
    else:
        print("Invalid Login") 
# Sign-up  Process 
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
                        print("Pin not correct") 
       elif choice_2 == "q": 
         print("Goodbye from Astroverse Bank")  






else:
        print("Invalid data") 
