class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        Pet.play(self)
        return self
    def feed(self):
        Pet.eat(self, 10)
        return self
    def bathe(self):
        Pet.noise(self)

class Pet:
    def __init__(self, name, type, tricks, health = 100, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health

    def sleep(self):
        print('sleeping')
        self.energy += 25
        return self
    def eat(self):
        print('eating')
        self.health += 10
        self.energy += 5
        print (self.health)
        print (self.energy)
        return self
    def play(self):
        print ('playing')
        self.health += 5
        print (self.health)
        return self
    def noise(self):
        print('Meow!')
        return self

    # def addHealth(self, amount):
    #     self.health += amount
    #     print (health)

ninja = Ninja('Rock', 'Lee', 'cat', 'salmon', 'cat food' )
cat = Pet('Whisker', 'cat', 'sleep')

# ninja.walk().feed().bathe()
cat.eat().play()
