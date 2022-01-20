import pandas


data = pandas.read_csv("Day25/Squirrel_Data_Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
report = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}


df = pandas.DataFrame(report)
df.to_csv("./Day25/Squirrel_Data_Analysis/report.csv")

# ### Alternative Solution #1
#
# def count_color(color):
#     squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == color]
#     return squirrels["Primary Fur Color"].size
# 
# 
# squirrel_data = pandas.read_csv("./Day25/Squirrel_Data_Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# 
# 
# grey_count = count_color("Gray")
# red_count = count_color("Cinnamon")
# black_count = count_color("Black")
# 
# 
# report = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [grey_count, red_count, black_count]
# }
# 
# 
# pandas.DataFrame(report).to_csv("./Day25/Squirrel_Data_Analysis/report.csv")

# ### Alternative Solution #2
#
# colors = pandas.read_csv("Day25/Squirrel_Data_Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"]
# 
# 
# grey_count = colors[colors == "Gray"].size
# red_count = colors[colors == "Cinnamon"].size
# black_count = colors[colors == "Black"].size
# 
# 
# report = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [grey_count, red_count, black_count]
# }
# 
# 
# pandas.DataFrame(report).to_csv("./Day25/Squirrel_Data_Analysis/report.csv")