# objects can have properties and methods
 # objects are made using classes
 # properties are things the class has
 # methods are things the class does

 # Using the class, you can create different instances/objects where the class is called.
 # can make each instance public or private
 # a constructor is a methods run when you're creating a new instance

 # child classes inherit all the attributes and methods of the parent class, so you dont need to rewrite code
 # anything private in the parent class doesnt get inherited without the 'protected' method


# Classes

# creating a class
class Athlete:
    def __init__(self, number, team):
        self.number=number
        self.team = team

class User:
    # constructor function
    def __init__(self,first_name, last_name, age, points):
        #attribute assignment
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.points = points
        # adding a reference to another class in a different file
        self.career = Athlete(23, 'Chicago Bulls')

    def showTeam(self):
        print (self.career.team)

    def greeting (self):
        print(f'Hello my name is {self.first_name}!')
        return self

    #adding the score method
    def score(self, amount): #takes an argument that is the amount of the score
        self.points += amount #the specific user's score points insceases by the specified amount
        print(f"{self.last_name}'s total score is now {self.points}")
        return self

    @classmethod
    def change(arg):
        pass

# instanciating the User class
michael = User('michael', 'jordan', 58, 32292)
steph = User('stephen', 'curry', 32, 18434)

michael.greeting()
steph.score(50)

# method chaining - must return self in method definition
steph.score(50).greeting()
michael.showTeam()
