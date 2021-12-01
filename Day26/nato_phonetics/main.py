import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(f"{key} : {value}")

# student_data_frame = pd.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#NATO PHONETICS NAME GENERATOR
####################################################################################

#TODO 1. Create a dictionary in this format:
# data = pd.read_csv('./phonetics.csv').to_dict()
###OR####
data = pd.read_csv('./phonetics.csv')

# result = {data['letter'][i]:data['code'][i] for i in range(len(data['letter']))}
###OR####
result = {row.letter : row.code for (index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter your name: ").replace(" ", "").upper()
user_input = [char for char in user_input]
final = [result[char] for char in user_input]
final = ' | '.join(final)

print(f"\n\nYour Name in Phonetics is : {final}\n\n")
