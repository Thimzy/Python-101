# print("boy")

# my_string = "i am a boy"
# print(my_string[3])
# formating string
# my_string = "This is 1840 naira"
# st2 = "This 570 is lovely"

# first_num = my_string[8:12]
# second_num = st2[5:8]
# added = int(first_num) + int(second_num)

# print(f"The sum of {first_num} and {second_num} is {added}")

# print(f"The sum of %s and %s is %d" % (first_num, second_num, added))

# print ("This is ayo's book")
# print('This is ayo\'s book')

# print("Dear, Buhari.\nPlease don't run for president again.\n\tYours in the country.\n\tAstroverse Team.")

# print("""This is a wonderful string




#                 Yours in country.
#                 The Astroverse team.""")
# a ="a aboy"
# print(a.rindex("a"))

# my_sentence = "A quick brown, fox jumps over, a lazy dog"

# a = my_sentence.split(",")
# print(a)

# num = ['0','4','3','2']

# otp = "".join(num)

# print(otp)

# s1 = "Ault"
# s2 = "Kelly"

# s3 = s1[0:2] + s2 + s1[2:4]
# print(s3)


# s1 = "Ault"
# s2 = "Kelly"

# print("Original Strings are", s1, s2)

# # middle index number of s1
# mi 







# str1 = "Welcome to USA. usa awesome, isn't it?"
# a = str1.lower().count("usa")
# print(f"The USA count is {a}")

# str1 = "Emma is a data scientist who knows Python. Emma works at google"
# print(str1.rindex("Emma"))

# strl = 'Emma-is-a-data-scientist'
# print(strl.replace('-', ' '))

# print(" ".join(strl.split('-')))

# strl = "/*Jon is @ developer & musician"
# ans = strl.replace("/*", "",).replace("@","a")
# print (ans)


######  LIST #######


# my_list = ["I", "am", "good"]
# a_list = ["She", "is", "a", "queen"]

# print(my_list + a_list)

# new_list = ["I", "am", "good", "she", "is", "a", "queen"]
# print(new_list [0: :2])

#Given the list below:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Get 5000 and 500 out of the list and add them together.
num1 = list1[2][2][0]
num2 = list1[2][3]
print(num1 + num2)