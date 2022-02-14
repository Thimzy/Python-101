import random

#...Bank App with Transaction data....#
data = {}
trans_data = {}

print("Welcome to the AstroBank App")
while True:
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        acc_num = input("Enter your account num:\n>")
        pin = input("Enter your pin:\n>")

        user = data.get(acc_num)

        if user and user['pin'] == pin:
            print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")

            while True:
                print("""\nWhat would you like to do?
                    Press 1 to withdraw
                    Press 2 to deposit
                    Press 3 to transfer
                    Press any other key to quit.""")

                user_input = input(">")

                if user_input == '1':
                    amount = int(input("How much?\n>"))
                    if amount >= user['bal']:
                        print("Insufficient Funds")
                    else:
                        user['bal']-=amount

                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "withdrawal"
                        }

                        trans_data[acc_num].append(detail)


                        print("Please take your cash")
                        print(f"Balance is {user['bal']}")

                elif user_input == '2':
                    amount = int(input("How much?\n>"))

                    user['bal']+=amount

                    #log transaction data
                    detail = {
                        "amount":amount,
                        "type": "credit",
                        "action" : "deposit"
                    }

                    trans_data[acc_num].append(detail)

                    print("Successful")
                    print(f"Balance is {user['bal']}")
                elif user_input == '3':
                    recepient_ = input("Enter recepient account\n>")
                    amount = int(input("How much?\n>"))

                    if user['bal'] < amount:
                        print("Insufficient Funds")

                    recepient = data.get(recepient_)
                    if recepient:
                        recepient['bal'] += amount
                        user['bal'] -=amount

                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "transfer"
                        }

                        trans_data[acc_num].append(detail)

                        detail_recepient = {
                            "amount":amount,
                            "type": "credit",
                            "action" : "transfer"
                        }

                        trans_data[recepient_].append(detail_recepient)

                        print("Successful")
                        print(f"Balance is {user['bal']}")
                    else:
                        print(f"Unable to fetch customer with account {recepient_}")

                else:
                    print("Good bye")
                    break
        else:
            print("Invalid Login")

    elif choice == 's':
        def name():
            name = input("Enter your name:\n>")
            if name is not []:
                print("Name must be string")
            name = input("Enter your name\n>")
        name()
        dob= input("Enter your date of birth:\n>")
        bvn= input("Enter your BVN:\n>")
        def pin():
            pin = (input("Enter your PIN:\n>"))
            if not any(char.isdigit() for char in pin):
                print("Pin must be numeric")
            pin = (input("Enter another pin:\n>"))
        pin()
        details = [('name', name), 
                ('dob', dob), 
                ('bvn', bvn), 
                ('pin', pin), 
                ('bal',0) 
                ]

        #generate account number
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num_list = ["3"]
        acc_num_list.extend([str(random.choice(num)) for _ in range(9)])


        acc_num = "".join(acc_num_list)

        data[acc_num] = dict(details)
        trans_data[acc_num] = []

        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else:
        break



print(data)
print(trans_data)
