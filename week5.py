# Assignment 1: Superhero Class with Inheritance
class Superhero:
    def __init__(self, name, power, secret_identity, weakness):
        self.name = name
        self.power = power
        self.__secret_identity = secret_identity  # Encapsulated attribute
        self.weakness = weakness

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def introduce(self):
        print(f"I am {self.name}, defender of justice!")

    def save_civilian(self, civilian):
        print(f"{self.name} rescues {civilian} from danger!")

    # Encapsulation methods
    def get_secret_identity(self):
        return self.__secret_identity

    def set_secret_identity(self, new_identity):
        self.__secret_identity = new_identity

class Villain(Superhero):
    def __init__(self, name, power, secret_identity, weakness, evil_plan):
        super().__init__(name, power, secret_identity, weakness)
        self.evil_plan = evil_plan

    # Polymorphism - override parent method
    def use_power(self):
        print(f"{self.name} unleashes {self.power} for destruction!")

    def reveal_plan(self):
        print(f"Evil scheme: {self.evil_plan}!")

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Helicopter(Vehicle):
    def move(self):
        print("Chopper hovering 🚁")

# Demonstration
if __name__ == "__main__":
    # Assignment 1 Demo
    print("🦸 Superhero System 🦹")
    hero = Superhero("Solar Flare", "heat manipulation", "Alex Ray", "absolute zero")
    villain = Villain("Dr. Chaos", "robot army", "Charles Smith", "EMP", "hack global networks")

    hero.use_power()
    villain.use_power()
    print(f"Hero's secret ID: {hero.get_secret_identity()}")
    villain.reveal_plan()

    # Activity 2 Demo
    print("\n🚦 Vehicle Movement 🚦")
    vehicles = [Car(), Plane(), Helicopter()]
    for vehicle in vehicles:
        vehicle.move()