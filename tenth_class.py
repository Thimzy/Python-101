from email.headerregistry import DateHeader
import os
import random

# #Create new directories
# BASE_DIR = os.getcwd()
# # new_dir = os.path.join(BASE_DIR, "new_dir")
# # os.mkdir(new_dir)

# #Checking files in a directories
# # for files in os.listdir(BASE_DIR):
# #     file_path = os.path.join(BASE_DIR, files)
# #     #print(file_path)
# #     if os.path.isfile(file_path):
# #         print(files)

# #Creating and changing directories
# # desktop_dir = "C:/Users/DELL/Desktop" #get desktop folder
# # os.chdir(desktop_dir)# change to desktop dir/folder
# # new_dir = os.path.join(desktop_dir, "python")#creating a new path

# # # os.mkdir(new_dir)# using the new path created to create a dir
# # os.chdir(new_dir)# make the new dir the current working directory (cwd)  dzdff 
# # print(new_dir)

# file = open("file.txt",mode="w")
# # file.write("\nPlenty things are happening")

# a = [1,2,3,5,6]
# file.write(f"{a}")

# file.close()

# file = open("file.txt",mode="r")
# data = eval(file.read())
# print(type(data))
# file.close()

# data.append(8)
# print(data)


data = {'John': ['1234', '{highscore}']}
while True:
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        username = input("Enter your username:\n>")
        password = input("Enter your pin:\n>")

        user = data.get(username, False)
        if user and user[0] == password:
            print("Welcome to RPS")
            print("""\nRules of the game:
            You are expected to choose between R or P or S.
            R for rock
            P for paper
            S for scissors

            Rock trumps Scissors
            Paper trumps Rock
            Scissors trumps Paper""")

            choices = ['r', 'p', 's']
            score = 0
            trial = 3

        while trial >=0:
            com_choice = random.choice(choices)
            player_choice = input("Choose:\n>").lower()

            if player_choice not in choices:
                print("Invalid entry")
                trial -=1
                print(f"{trial} trail(s) left")
            else:
                if player_choice == 'r' and com_choice == 'p':
                    print(f"Computer selected {com_choice.upper()}\nYou lose.")
                    trial -=1
                    print(f"{trial} trail(s) left")
                
                elif player_choice == 'p' and com_choice == 's':
                    print(f"Computer selected {com_choice.upper()}\nYou lose.")
                    trial -=1
                    print(f"{trial} trail(s) left")

                elif player_choice == 's' and com_choice == 'r':
                    print(f"Computer selected {com_choice.upper()}\nYou lose.")
                    trial -=1
                    print(f"{trial} trail(s) left")

                elif com_choice == 'r' and player_choice == 'p':
                    print("You win")
                    score +=2
                    trial +=1
                    print(f"{trial} trail(s) left")

                elif com_choice == 'p' and player_choice == 's':
                    print("You win")
                    score +=2
                    trial +=1
                    print(f"{trial} trail(s) left")

                elif com_choice == 's' and player_choice == 'r':
                    print("You win")
                    score +=2
                    trial +=1
                    print(f"{trial} trail(s) left")
                
                else:
                    print("It's a tie")
                    trial -=1
                    print(f"{trial} trail(s) left")
                

        print(f"\nYour score is {score}")
        print("Game over!")
        highscore = score
        if highscore >= user[1]:
            user[1] = highscore
            print(f"\nYour new high score is {highscore}")

    
    elif choice == 's':
        username = input("Enter your username:\n>")
        password= input("Enter your password:\n>")
        highscore = 0

        data[username] = [password, highscore]
        print(f"\nSignin successful")
    
    else:
        break
print(data)
