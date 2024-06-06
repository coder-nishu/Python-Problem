string = "you asre from daffodil uni. you are currently studying 5th semester."
x = string.replace("5th","7th")
print(x) 

for i in string:
    if i == "5th":
        i = "7th"
print(string)