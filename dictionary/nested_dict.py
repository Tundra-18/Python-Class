my_class = {
    "student_1" : {
        "name" : "Zaw Ye Naung",
        "age": 23,
        "address" : "Insein"
    },

    "student_2" : {
        "name" : "Sit Paing",
        "age" : 23,
        "address" : "YaNGON"
    },

    "student_3" : {
        "name" : "Ko Ko",
        "age" : 26,
        "address" : "Mdy"
    }
}
print(my_class)
print(my_class["student_3"]["name"])

for x,y in my_class.items():
    print("\n" + x)
    for z in y:
        print(z + f"= {y[z]}")