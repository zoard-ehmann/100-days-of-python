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

# DataFrame
data = pandas.read_csv("./Day25/Reading_CSV/weather_data.csv")

# Series
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])    # Treating data as a dictionary
print(data.condition)       # Treating data as an object

# Get Data in Row
print(data[data.day == "Monday"])

# Get the day which has the highest temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

# Create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./Day25/Reading_CSV/new_data.csv")