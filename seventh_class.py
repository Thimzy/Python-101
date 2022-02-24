from datetime import datetime
import random
# import time   
# num = range(10,50)
# my_filter = filter(lambda x:x % 2!=0, num)
# print(list(my_filter))

# text = "Www.HackerRank.com"
# print(text.swapcase())

# a ="".join([i.upper() if i.islower() else i.lower() for i in text])
# print(a)

# print("Hello there!")
# time.sleep(2.5)
# print("Done!")
# random.seed(1)
# my_num = list(range(1,11))

# random.shuffle(my_num) #shuffles the list
# print(my_num)
# data = random.sample(my_num, 3)#get a sample of k items from our overall population
# print(data)

# today = datetime.today().isoweekday()
# today = datetime.today().weekday()
# today = datetime.today().month()
# today = datetime.today().year()
# today = datetime.today().hour()

# today = datetime.today()
# print(datetime.strftime(today, "%A, %dth of January, %Y"))
# print(datetime.strftime(today, "%A - %d - %b - %Y"))
# print(datetime.strftime(today, "%a, %b %dth %Y"))
# print(datetime.strftime(today, "Today is the %dth day of %b. %Y "))
# print(datetime.strptime("21-Jan-22 8:10:40", "%d-%b-%y %H:%M %S"))

# write a fuction that takes in an integer and return true or false if the integer is a prime number

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
        name = input("Enter your name:\n>")
        dob= input("Enter your date of birth:\n>")
        bvn= input("Enter your BVN:\n>")
        pin = (input("Enter another pin:\n>"))
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