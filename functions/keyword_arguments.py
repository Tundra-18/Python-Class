# def my_function(name,age,address):
#     print("Name:", name)
#     print("Age:", age)
#     print("Address : ",address)
#
# my_function(address="Insein",name="Zaw",age=56)

# def introduce(name, city):
#     print(f"My name is {name} and I live in {city}.")
#
# introduce("John", "New York")
# introduce(city="Yangon", name="Aye Aye")


def greet(name="Guest"):
    return f"Name is {name}"

greet() # default value
greet("Su Su")

print(greet("Su Su"))