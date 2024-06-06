#1st time it use to format string
letter = "my name is {} and i am from {}"
country = "bangladesh"
name = "nishat"
print(letter.format(name,country))

#now we can use f string
print(f"my name is {name} & i am from {country}")

price = 29.00567
print(f"The car price is {price:0.2f}.")

#to make string
print(type(f"{5*4}"))

#to avoid f string.just use double curly braces
print(f"my name is {{name}} & i am from {{country}}")