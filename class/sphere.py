class Sphere:
    def __init__(self, radius):
        self.sphere_radius = radius

    def volume(self):
        return (4 / 3) * 3.142 * (self.sphere_radius ** 3)

r = float(input("Enter radius : "))
print(f"The radius is {r} m.\n")

s1 = Sphere(r)
print(f"The volume of a sphere is {s1.volume()} m cube.")



