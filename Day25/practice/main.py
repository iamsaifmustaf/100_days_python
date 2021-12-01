import pandas as pd

# import csv

# with open("./weather_data.csv", "r") as data_file:      

#     file_content = csv.reader(data_file)
#     temperatures = []

#     for row in file_content:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)

# print(temperatures)

data = pd.read_csv("weather_data.csv")
max_temp = data["temp"].max()
day_max_temp = data[data.temp == max_temp]['condition']


print(day_max_temp)
