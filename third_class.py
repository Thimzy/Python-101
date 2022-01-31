# List Methods ##
#.....Index Method.......#

# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# print(color_list.index('Red'))

# #......How to add a new list......#
# print("Welcome to the astroverse!")
# # choice = input("Enter your favourite color:\n>")
# # position = int(input("Enter the position:\n>"))

# # color_list.append(choice)

# # color_list.extend(position, choice)
# # print(color_list)

# data = input("Enter your colours seperated by space:\n>")

# cleaned_data = data.split
# print(cleaned_data)

# color_list.extend(cleaned_data)
# print(color_list)

#.....How to remove element from a list......#
#.....Pop.....#
# la = [0, 2, 3, 4,]
# la.pop(2)
# print(la)


# li = [0, 2, 9, 8]
# a = li.pop(1)
# li.append(a)
# print(li)

#......Remove.....#
# li = [0, 2, 9, 8]
# li.remove(9)
# print(li)



#.....Copy......#
# a = [1, 5, 7, 2]
# b = a
# c = a.copy()
# a.remove(5)
# print(b)
# print(c)

#....TUPLES......#
# my_tuple = 1,2,3,4,5,6
# print(my_tuple)


#....SET......#
# a = {1,2,4,6}
# b = {2,4,1,5}

# # c = a.difference(b)
# c = a.symmetric_difference(b)
# b.intersection_update(a)
# print(c)


# english = input("Enter roll number for english students:\n>")
# french = input("Enter roll numbers for french students:\n>")

# english_list = english.split()
# french_list = french.split()

# englist_set = set(english_list)
# french_set = set(french_list)

# total = englist_set.symmetric_difference(french_set)

# print(len(total))

# eng = {1,2,3,4,5,6,7,8,9}
# french = {10,1,2,3,11,21,55,6,8}
# c = eng.symmetric_difference(french)
# ans = len(c)
# print(ans)



# eng = {1,2,3,4,5,6,7,8,9}
# french = {10,1,2,3,11,21,55,6,8}
# c = eng.union(french)
# ans = len(c)
# print(ans)

# print(2%6)