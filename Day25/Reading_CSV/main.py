# with open("./Day25/Reading_CSV/weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     
# 
# print(data)

# import csv
# 
# 
# with open("./Day25/Reading_CSV/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if data.line_num != 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
import pandas


data = pandas.read_csv("./Day25/Reading_CSV/weather_data.csv")
print(data["temp"])