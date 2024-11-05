class Insect:
    def __init__(self, name, speed, mass, area, pop):
        if speed <= 0 or mass <= 0:
            raise ValueError("Speed and mass must be positive values.")

        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.area = area
        self.population = pop

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_mass(self):
        return self.__mass



    def __str__(self):
        return (f"Name: {self.__name}\nSpeed: {self.__speed} m/s\nMass: {self.__mass}\n"
                f"Area: {self.area}\nPopulation: {self.population}")

    def __repr__(self):
        return f"Insect({self.__name}, {self.__speed}, {self.__mass}, \"{self.area}\", {self.population})\n"

    def __del__(self):
        print("The object is deleted.")


insect = Insect("Monarch Butterfly", 3, 0.5, "North America", 21)
print(insect)
print("repr: " , repr(insect))

insect1 = Insect("Bee", 19, 200, "Almost everywhere", 101)
print(insect1)
print("repr: " , repr(insect1))

insect2 = Insect("Spider", 0.53, 0.2, "Almost everywhere", 210000)
print(insect2)
print("repr: " , repr(insect2))

