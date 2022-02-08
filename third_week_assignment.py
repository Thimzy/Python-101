import random
import time


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
        print(user)
        print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
#Withdraw, deposit and transfer

        print("""\nWhat would you like to do?
              Press 1 to withdraw
              Press 2 to deposit
              press 3 to transfer
              Press any other key to quit. """)

        user_input = input(">")

        if user_input == "1":
            amount = int(input("How much?\n>"))
            if amount >= user['bal']:
                print("Insufficient Funds")
            else:
                user['bal']-= amount
                print("Please take your cash")
                print(f"Balance is {user['bal']}")

        elif user_input == '2':
            amount = int(input("How much?\n>"))

            user['bal']+= amount
            print ("Succesful")
            print(f"Balance is {user['bal']}")
        

        if user_input == '3':
            trans_account = input("Enter the account you wish to transfer to\n>")
            trans_account = data.get(trans_account)
            if trans_account == acc_num:
                print("You can't transfer to your own account")
            else:
                amount = int(input("How much do you want to transfer\n>"))
                pin = input("Enter your pin\n>")
                if amount <= user['bal']:
                    user["bal"] -= amount 
                    trans_account["bal"] +=amount
                    print('......Processing Transaction......')
                    time.sleep(3)
                    print("Transaction successful")
        else:
            print("Goodbye")
    else: 
        print("Invalid Login")


elif choice == 's':
    name = input("Enter your name:\n>")
    dob = input ("Enter your date of birth:\n>")
    bvn = input ("Enter your BVN\n>")
    pin = input ("Enter your PIN\n>")
    details = [('name', name), 
               ('dob', dob), 
               ('bvn', bvn), 
               ('pin', pin), 
               ('bal', 0)
            ]

    num = [1,2,3,4,5,6,7,8,9,0]
    acc_num_list = 3
    acc_num_list = [str(random.choice(num)) for _ in range(10)]
    # print(acc_num_list)
    acc_num = "".join(acc_num_list)

    data[acc_num] = dict(details)
        
else: 
    print("Invalid input")

print(data)