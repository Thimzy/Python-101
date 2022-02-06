import random
from statistics import median, variance
import time


# print("Welcome to RPS")
# print("""\nRules of the game:
# You are expected to choose between R or P or S.
# R for rock
# P for paper
# S for scissors

# Rock trumps Scissors
# Paper trumps Rock
# Scissors trumps Paper""")

# choices = ['r', 'p', 's']
# score = 0
# trial = 3


# while trial >0:
#     com_choice = random.choice(choices)
#     player_choice = input("Choose:\n>").lower()

#     if player_choice not in choices:
#         print("Invalid entry")
#         trial -=1
#         print(f"{trial} trail(s) left")
#     else:
#         if player_choice == 'r' and com_choice == 'p':
#             print(f"Computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trail(s) left")
        
#         elif player_choice == 'p' and com_choice == 's':
#             print(f"Computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trail(s) left")

#         elif player_choice == 's' and com_choice == 'r':
#             print(f"Computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trail(s) left")

#         elif com_choice == 'r' and player_choice == 'p':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trail(s) left")

#         elif com_choice == 'p' and player_choice == 's':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trail(s) left")

#         elif com_choice == 's' and player_choice == 'r':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trail(s) left")
        
#         else:
#             print("It's a tie")
#             trial -=1
#             print(f"{trial} trail(s) left")

# print(f"\nYour high score is {score}")
# print("Game over!")



# user_input = input("Enter your numbers seperated by comma\n>")
# num = [int(i) for i in user_input.split(",")] # Using list comprehension

# alternatively, we can use mapping to map a finction to list

# num = list(map(lambda x: int(x),user_input.split(",")))
# print(num)
# print(user_input.split(","))


## Calculating the mean #
# mean = sum(num)/len(num)


## Calcuting the median #
# num.sort()

# midpoint = len(num)//2
# if len(num)%2 == 0:
#     median = (num[midpoint] + num[midpoint-1])/2
# else:
#     median = num[midpoint]



# Calculating the mode
# freq = {}
# for i in num:
#     freq[i] = freq.get(i,0) + 1

# mode = max(freq, key=lambda x:freq[x])


# ## Standard deviation

# standard_deviation = (sum([(x-mean)**2 for x in num])/len(num))**0.5

# ##Variance
# print("Calculating........\n>")
# time.sleep(3)
# print("View results below:\n>")

# variance = standard_deviation**2
# print(f"The mean is {round(mean, 2)}")
# print(f"The median is {median}")
# print(f"The mode is {mode}")
# print(f"The standard_deviation is {round(standard_deviation,2)}")
# print(f"The variance is {round(variance,2)}")

# print(dict(zip([1,2,3,4,5] [1,4,9,16,25])))



# principal = float(input('Enter the priniciple amount: \n>'))
# time = float(input('Enter the time: \n>'))
# rate = float(input('Enter the rate: \n>'))

# simple_interest = (principal*time*rate)/100
# print('Simple interest is:', simple_interest)