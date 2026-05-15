class Rectangle:
    def __init__(self, width, height):
        self.rectangle_width = width
        self.rectangle_height = height

    def area(self):
        return self.rectangle_width * self.rectangle_height

    def perimeter(self):
        return (self.rectangle_width + self.rectangle_height) * 2

width_input = float(input("Enter Width : "))
height_input = float(input("Enter Height : "))

print(f"\nWidth is {width_input} m.")
print(f"Height is {height_input} m.")

r1 = Rectangle(width_input,height_input)
print(f"\nArea is {r1.area()} meter square.")
print(f"Perimeter is {r1.perimeter()} meter.")

