import pandas as pd
import random

##############################################################
#List Comprehension
##############################################################

# numbers = range(0,500)
# numbers_squared = [num for num in numbers if num % 2 == 0]
# print(numbers_squared)


# with open('file1.txt') as file1:
#     file_1_data = file1.readlines()

# with open('file2.txt') as file2:
#     file_2_data = file2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]

# print(result)

##############################################################
#Dictionary Comprehension
###############################################################

# names = ['Alex' , 'Beth' , 'Caroline' , 'Eleanor' , 'Freddie']

# student_scores = {name:random.randint(50,100) for name in names}

# passed_students = {student:score for (student,score) in student_scores.items() if score > 50}

# print(student_scores)
# print(passed_students)

###############################################################

# data = pd.read_csv('./50_states.csv').to_dict()

# states = {number : state for (number,state) in data['state'].items() if len(state) < 5}

# print(states)

###############################################################


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# words_list = sentence.split(' ')

# words_length = [len(word) for word in words_list]

# result = {words_list[i]:words_length[i] for i in range(len(words_list))}

# print(result)

###############################################################

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# weather_f = { d : int((temp*(9/5) + 32)) for ( d , temp ) in weather_c.items() }

# print(weather_f)

###############################################################

student_dataframe = pd.DataFrame(weather_c.items())
print(student_dataframe)