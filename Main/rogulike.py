# Goals:
# description :
# lore :
# you are a hero in middle ages and you went on a trip to other city and choose the short route, on the way you accidentally fell into some
# kind of cave. It's inded some kind of an old Temple, with rooms and doors, you have some hope that there is an exit some where. You are
# brave so you decide to open some of the doors to see what's behind them
#
# on the beginning you choose the name of your character, choose type of your character (warrior, archer, mage)
# choose one of starting weapons
#
# logic :
# player visits a room which has several places for door, and for and item/monster (trader spawns in empty room), map is 5x5 rooms one has an
#
# classes : character, trader, monster, door, room, ?fight?, item(potion, equipable)
# character :
# name, type, pet, weapon, inventory, equipped_items, HP, Attack, armour, money,

# monster :
#  Hp, Attack, loot distance to middle (to know difficulty),
#
# ideas :
# keep track of route to know which rooms are empty, maybe display a map(on command $map)
#
# skills(frost mage/fire mage)(archer with evade/...)...
# critical hits
# damage range (6 is base -> 6<attack<8) crit-> ~12
# armor, block chance

# implement help command

# create saving system with text file
#

# starting goals :
# Character, monster classes, try to fight
#
def initiate_game_over():
    print("Game over...")


def Victory():
    print("You won this fight")


def fight(character, monster):
    while character.fighting:
        character.attack(monster)
        if not monster.fighting:
            break
        input()
        monster.attack(character)
        input()

class Character:

    def __init__(self, name, armor, hp, base_damage):
        self.name = name
        self.damage = base_damage
        self.hp = hp
        self.armor = armor
        self.alive = True
        self.fighting = True

    def attack(self, opponent):
        opponent.defend(self)

    def defend(self, opponent):
        self.hp -= opponent.damage
        if not self.alive:
            self.fighting = False
        print('{} was attacked by {} and took {} damage. \nHe has {} hit points.'.format(self.name, opponent.name,
                                                                                         opponent.damage, self.hp))

    def dead(self):
        print('The ' + self.name + ' is now dead.')
        self.alive = False
        self.fighting = False
        initiate_game_over()


class Monster:

    def __init__(self, name, armor, hp, base_damage):
        self.name = name
        self.damage = base_damage
        self.hp = hp
        self.armor = armor
        self.alive = True
        self.fighting = True

    def attack(self, opponent):
        opponent.defend(self)

    def dead(self):
        print('The ' + self.name + ' is now dead.')
        self.alive = False
        self.fighting = False
        Victory()

    def defend(self, opponent):
        self.hp -= opponent.damage
        if self.hp <= 0:
            opponent.fighting = False
            self.dead()
        else:
            print('{} was attacked by {} and took {} damage. \nHe has {} hit points.'.format(self.name, opponent.name,
                                                                                             opponent.damage, self.hp))


monster1 = Monster('Snail', 3, 24, 2)

main_character = Character('hoodrick', 2, 20, 15)

input('Press enter to start the fight...')
print('Starting the fight..')

fight(main_character, monster1)
