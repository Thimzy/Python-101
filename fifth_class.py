import random
import time


data = {}
trans_data = {}


print("Welcome to the AstroBank App")
while True:
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
            while True:
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

                    user['bal']+= amount
                    #log transaction data
                    detail = {
                                "amount":amount,
                                "type": "credit",
                                "action": "deposit"
                            }

                    trans_data[acc_num].append(detail)
                    print ("Succesful")
                    print(f"Balance is {user['bal']}")
                

                elif user_input == '3':
                    trans_account = input("Enter the account you wish to transfer to\n>")
                    recepient = data.get(trans_account)
                    if trans_account == acc_num:
                        print("You cant transfer to your own account")
                    else:
                        amount = int(input("How much do you want to transfer\n>"))
                        if amount <= user['bal']:
                            user["bal"] -= amount 
                            recepient["bal"] +=amount
                            #log transaction data
                            detail = {
                                "amount":amount,
                                "type": "debit",
                                "action": "transfer"
                            }

                            trans_data[acc_num].append(detail)

                            detail_recepient = {
                                "amount":amount,
                                "type": "credit",
                                "action": "transfer"
                            }

                            trans_data[trans_account].append(detail_recepient)

                            print('......Processing Transaction......')
                            time.sleep(3)
                            print("Transaction successful")
                        else:
                            print(f"Unable to fetch customer with account {trans_account}")
                else:
                    print("Goodbye")
                    break
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
        acc_num_list = [str(random.choice(num)) for _ in range(10)]
        # print(acc_num_list)
        acc_num = "".join(acc_num_list)

        data[acc_num] = dict(details)
        trans_data[acc_num] = []
        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else: 
        break

print(data)
print(trans_data)


# # num = [1,2,3,4,5,6,7,8,9,0]
# # print("Guess World")
# # random.shuffle(num)
# # choice = 3

# # trial = 3
# # score = 0

# # # for i in range(10000000000000000000000000):
# # #     if trial == 0:
# # #         print("Game Over!")
# # #         print(f"Your score is {score}")
# # #         break
# # while trial != 0:
# #     choice = random.choice(num)
# #     print(choice)
# #     play = int(input('Enter your number\n>'))
# #     if play == choice:
# #         trial +=1
# #         score +=3
# #         print("Correct!")
# #         print("You have been given an extra trial")
# #         print("Yayyyy! ????????")
# #     else:
# #         trial -=1
# #         print("Incorrect!")
# #         print(f"You have {trial} trial(s) left")
# #         print("Game Over")
# #         print(f"Your score is {score}")
#     # print(choice)
# while True:
#     user_choice = input("Enter a choice (rock, paper, scissors):\n> ")

#     game = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(game)
#     print(f"\nYou choose {user_choice}, computer choose {computer_choice}:\n")

#     if user_choice == computer_choice:
#         print(f"Both players selected {user_choice}. It's a tie!")
#     elif user_choice == "rock":
#         if computer_choice == "scissors":
#             print("Rock smashes scissors You won")
#         else:
#             print("Paper covers rock You lost.")
#     elif user_choice == "paper":
#         if computer_choice == "rock":
#             print("Paper covers rock You won")
#         else:
#             print("Scissors cuts paper You lost.")
#     elif user_choice == "scissors":
#         if computer_choice == "paper":
#             print("Scissors cuts paper You won.")
#         else:
#             print("Rock smashes scissors You lost.")
    
#     play_again = input("Play again? (y/n):\n>")
#     if play_again.lower() != "y":
#         print("Game Over")
#         break

