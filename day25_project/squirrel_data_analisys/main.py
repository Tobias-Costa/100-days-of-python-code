import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# squirrel_colors_list = data["Primary Fur Color"].to_list()

# gray_squirrel_count = squirrel_colors_list.count("Gray")
# red_squirrel_count = squirrel_colors_list.count("Cinnamon")
# black_squirrel_count = squirrel_colors_list.count("Black")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_colors_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

squirrel_colors = pd.DataFrame(squirrel_colors_dict)
squirrel_colors.to_csv("squirrel_count.csv")