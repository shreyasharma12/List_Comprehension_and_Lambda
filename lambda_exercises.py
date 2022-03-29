""" ############################### 1) ######################################################################################
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""
nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, nums_list))
print(even_list)

odd_list = list(filter(lambda x: x % 2 == 1, nums_list))
print(odd_list)

""" #################################################### 2) #################################################################
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

characters = list(filter(lambda x: (len(x) == 6), weekdays))
print(characters)

""" ################################################### 3) ###################################################################
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
"""

original_list = ["orange", "red", "green", "blue", "white", "black"]
removed_list = list(filter(lambda x: ("a" not in x), original_list))
print(removed_list)

""" ################################################### 4) ####################################################################
remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

final_list = list(filter(lambda x: x not in list2, list1))
print(final_list)

""" ################################################# 5) #####################################################################
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]
"""

colors_list = ["red", "black", "white", "green", "orange"]
substring = list(filter(lambda x: "ack" in x, colors_list))
print(substring)

substring1 = list(filter(lambda x: "abc" in x, colors_list))
print(substring1)

""" ################################################# 6) ########################################################################
check whether a given string contains a capital letter, a lower case letter, 
a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""

password = input('Please enter a new password: ')
password_verification = [
    lambda x: any(x.isupper() for x in password), 
    lambda x: any(x.islower() for x in password), 
    lambda x: any(x.isdigit() for x in password), 
    lambda x: any(x.isalpha() for x in password),
    lambda x: len(x) >= 8]

if(any(x.isupper() for x in password) 
and any(x.islower() for x in password) 
and any(x.isdigit() for x in password)
and any(x.isalpha() for x in password) 
and len(password) >= 8):

    print("Password is verified.")
else: 
     print('Password has not been verified. Please try another password.')

""" ################################################## 7) ##########################################################################
Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key = lambda x: x[1])
print(original_scores)