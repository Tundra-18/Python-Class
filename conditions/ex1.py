name = input("Enter name : ").strip().title()
age = int(input("Enter age : "))
gender = input("Enter gender : ")
height = float(input("Enter height : "))

match gender:
    case "male" | "Male":
        print(f"\nHis name is {name} and {age} years")
        print(f"His height is {height}")
    case "female" | "Female":
        print(f"\nHer name is {name} and {age} years")
        print(f"Her height is {height}")
    case _:
        print("Invalid gender!")
