class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.energy = 50
        self.health = 100



    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.noise)
        return self

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self



    # def addHealth(self, amount):
    #     self.health += amount
    #     print (health)


yuri = Pet('Whiskera', 'cat', 'sleeps', 'Meow!')
cole = Ninja('Rock', 'Lee', yuri , 'salmon', 'cat food' )


cole.walk().feed()
# cat.eat().play()
