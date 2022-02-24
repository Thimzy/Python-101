# # import os

# # BASE_DIR = os.getcwd()
# # # new_dir = os.path.join(BASE_DIR, "new_dir")
# # # os.mkdir(new_dir)

# # # for file in os.listdir(BASE_DIR):
# # #     file_path = os.path.join(BASE_DIR, file)
# # #     # print(file_path)
# # #     if os.path.isfile(file_path):
# # #         print(file)

# # desktop_dir = "C:/Users/BudgIT Guest/Desktop" #get desktop folder
# # os.chdir(desktop_dir) #change to desktop dir/folder
# # new_dir = os.path.join(desktop_dir, "python") #creating a new path

# # # os.mkdir(new_dir) #using new path created to create a dir
# # os.chdir(new_dir) #make the new dir the current working directory (cwd)
# # print(new_dir)

# file = open("file.txt",mode="w" )
# # file.write("\nPlenty things are happening")
# a = [1,2,3,5,6]
# file.write(f"{a}")

# file.close()

# file = open("file.txt",mode="r" )
# data = eval(file.read())
# print(type(data))
# file.close()

# data.append(8)
# print(data)

import random

def play_game():
    choices = ['r', 'p', 's']
    score = 0
    trial = 3

    while trial >0:
        com_choice = random.choice(choices)
        player_choice = input("\nChoose:\n>").lower()

        if player_choice not in choices:
            print("Invalid entry")
            trial -=1
            print(f"{trial} trial(s) left")
        
        else:  
            if player_choice == 'r' and com_choice == 'p':
                print(f"Computer selected {com_choice.upper()}\nYou lose.")
                trial -=1
                print(f"{trial} trial(s) left")
            
            elif player_choice == 'p' and com_choice == 's':
                print(f"Computer selected {com_choice.upper()}\nYou lose.")
                trial -=1
                print(f"{trial} trial(s) left")
            elif player_choice == 's' and com_choice == 'r':
                print(f"Computer selected {com_choice.upper()}\nYou lose.")
                trial -=1
                print(f"{trial} trial(s) left")
            elif com_choice == 'r' and player_choice == 'p':
                print("You win")
                score +=2
                trial +=1
                print(f"{trial} trial(s) left")
            elif com_choice == 'p' and player_choice == 's':
                print("You win")
                score +=2
                trial +=1
                print(f"{trial} trial(s) left")
            elif com_choice == 's' and player_choice == 'r':
                print("You win")
                score +=2
                trial +=1
                print(f"{trial} trial(s) left")
            else:
                print("It's a tie")
                trial -=1
                print(f"{trial} trial(s) left")
    return score

def user(action):
    username = input("Username: ")
    password = input("Password: ")

    if action == "login":
        user_ = data.get(username)
        if user_ and user_[0] == password:
            print(f"Welcome, {username}!\nYour current high score is {user_[1]}")
            return user_
        print("Invalid username and password")
        return 
    
    elif action == "signup":
        if username in data.keys():
            print("Username already taken ):")
            return
        data[username] = [password, 0]
        print("Succesfully created account!")
        return 

file = open("file.txt", "r")
data = eval(file.read())
file.close()


print("Welcome to RPS")
print("""\nRules of the game:
You are expected to choose between R or P or S.
R for rock
P for paper
S for scissors
Rock trumps Scissors
Paper trumps Rock
Scissors trumps Paper""")


print("Enter l to login, s to signup and any other key to quit:")
choice = input(">")

if choice == "l":
    user_data = user(action="login")
    score = play_game()
    if score > user_data[1]:
        print("Tadaaaa!!!, you have a new high score!")
        user_data[1] = score
elif choice=="s":
    user(action="signup")
    
    

  

file = open("file.txt", "w")
file.write(f"{data}")
file.close()  