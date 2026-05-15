class Student:
    def __init__(self):
        self.__mark = 0

    def set_mark(self, value):
        if 0 <= value <= 100:
            self.__mark = value
        else:
            print("Invalid mark")

    def get_mark(self):
        print(f"The mark is",self.__mark)

s = Student()
s.set_mark(95)
s.get_mark()

