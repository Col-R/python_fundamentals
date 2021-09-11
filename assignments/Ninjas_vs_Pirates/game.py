from classes.ninja import Ninja
from classes.pirate import Pirate


michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

def p1_move():
    move = input('Press 1 to attack, 2 to show stats ')
    print (move)
    if move == '1':
        michelangelo.attack(jack_sparrow)
        # TODO: Add reference to critical hit function based on random rng
        print('Michelanglo attacks')

    elif move == '2':
        michelangelo.show_stats()
        p1_move()
    if jack_sparrow.health <= 0:
        print('Ninjas win!')
        exit()
    p2_move()
def p2_move():
    move = input('Press 1 to attack, 2 to show stats ')
    print (move)
    if move == '1':
        jack_sparrow.attack(michelangelo)
        print('Jack Sparrow attacks')
    elif move == '2':
        jack_sparrow.show_stats()
        p2_move()
    if michelangelo.health <= 0:
        print('Pirates win!')
        exit()
    p1_move()

p1_move()
p2_move()



# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
