class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        Pet.play(Ninja)
    def feed(arg):
        pass
    def bathe(arg):
        pass

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 10
        self.health = 10

    def sleep(arg):
        pass
    def eat(arg):
        pass
    def play(self):

        self.health +=5
        return self
    def noise(self):
        print('Meow!')

ninja = Ninja('Rock', 'Lee', 'cat', 'salmon', 'cat food' )
cat = Pet('Whisker', 'cat', 'sleep')

ninja.walk()
