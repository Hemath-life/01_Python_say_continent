"""
1. wite down the 7 continents list 
2. get x and y coordinate in image add to cv
3. making the 7 ,x and y  to cv 

"""
import pandas
continent_names = [
    "North America",
    " South America",
    "Africa",
    "Europe",
    "Asia",
    "Australia/Oceania",
    "Antarctica",
]

x = [-370.0, -208.0, 36.0, 31.0, 204.0, 351.0, -38.0]
y = [125.0, -108.0, -43.0, 89.0, 93.0, -138.0, -353.0]


data_dict = {"continents": continent_names, "x": x, "y": y}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("./continent_names.csv")