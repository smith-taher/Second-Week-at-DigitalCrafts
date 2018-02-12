"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        #self.attack = attack
    def attack(self, goblin):
        #self.attack = attack
        #Hero.attack(Goblin)
        the_goblin.health -= self.power
    def alive(self, cls):
        if the_hero.health <= 0:
            print "You are dead."  
         
class Goblin():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        #self.attack = attack
    def attack(self, hero):
        the_hero.health -= self.power
    def alive(self, cls):
        if the_goblin.health <= 0:  
            print "The goblin is dead."

the_hero = Hero(10,3)
the_goblin = Goblin(6,2)
       
# def main():
#     Hero.health = 10
#     Hero.power = 5
#     Goblin.health = 6
#     Goblin.power = 2

while the_goblin.alive > 0 and the_hero.alive > 0:
    print "You have %d health and %d power." % (the_hero.health, the_hero.power)
    print "The goblin has %d health and %d power." % (the_goblin.health, the_goblin.power)
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        the_hero.attack(the_goblin)
        print "You do %d damage to the goblin." % the_hero.power
        #if the_goblin.health <= 0:
            #print "The goblin is dead."
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if the_goblin.health > 0:
        # Goblin attacks hero
        the_goblin.attack(the_hero.health)
        print "The goblin does %d damage to you." % the_goblin.power
        # if the_hero.health <= 0:
        #     print "You are dead."
        
# main()
