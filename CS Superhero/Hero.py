class Hero:
    def __int__(self, name, starting_health=100):
    
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    if __name__ == "__main__":
        my_hero = Hero("Grace Hopper", 200)
        hero1 = Hero("Wonder Woman")
        hero2 = Hero("Dumbledore")
        print(my_hero.name)
        print(my_hero.current_health)

    import random

class Ability:

    if __name__ == "__main__":
        ability = Ability("Debugging Ability", 20)
        print(ability.name)
        print(ability.attack())
        def attack(self):

            random_value = random.randint(0,self.max_damage)
            return random_value
        def __init__(self, name, max_damage):
            self.name = name
            self.max_damage = max_damage

class Armor:
    def  __init__(self, name, max_block):
        '''Instantiate instance propertiesdatetime A combination of a date and a time. Attributes: ()           
           name: String
           max_block: Integer
        '''
        pass
    def blcok(self):
        '''
        Return a random value between 0 and the initialized max_block strength. 
        '''
        pass

    if __name__ == "__main__":
        armor = Armor("Debugging Shield", 10)
        print(armor.name)
        print(armor.block())


from ability import ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name()
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    if __name__ == "__main__":
        ability = Ability("Great Debugging", 50)
        another_ability = Ability("Smarty Pants", 90)
        hero = Hero("Grace Hopper", 200)
        hero.add_ability(ability)
        hero.add_ability(another_ability)
        print(hero.abilities)
        print(hero.attack()





    def attack(self):
        total_damage = 0
            for ability in self.abilities:
                total_damage +=ability.attack()
            return total_damage




   def is_alive(self):
       pass


   if ___name__ == "__main__":
       hero = Hero("Grace Hopper", 200)
       hero.take_damage(150)
       print(hero.is_alive())
       hero.take_damage(15000)
       print(hero.is_alive())
class Weapon(Ability):
    def attack(self):
        pass

from weapon import weapon
class Hero:
    def add_weapon(self, weapon):
        pass

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

class Team: 
    def __init__(self, name):
        self.name = name()
        self.heroes = list()

def remove_hero(self, name):
    foundHero = False
    for hero in self.heroes:
        if hero.name == name:
            self.heroes.remove(hero)
            foundHero = True
    if not foundHero:
        return 0

def view_all_heroes(self):
    pass

def add_hero(self, hero)
    pass

def __init__(self, name, health=100):
    self.deaths = 0
    self.kills = 0

def add_kill(self, num_kills):
    self.kills += num_kills

def add_death(self, num_deaths):
    pass

def stats(self):
    for hero in self.heroes:
        kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))

def attack(self, other_team):
    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
        living_heroes.append(hero)
    for hero in other_team.heroes:
        living_opponents.append(hero)
    while len(living_heroes) > 0 and len(living_opponents)>


from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team



def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = input(
        "What is the max damage of the ability?  ")
    
    return Ability (name, max_damage)

def create_weapon(self):
    pass

def create_armor(self):
    pass


def create_hero(self):
    hero_name = input("Hero name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item !+ "4":
        add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
        if add_item == "1"
        elif add_item == "2":
        elif add_item == "3":
    return hero

def buld_team_one(self):
    num0fTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_one.add_hero(hero)

def build_team_two(self):
    pass

def team_battle(self):
    pass

print("\n")
print(self.team_one.name + " statistics: ")
self.team_one.stats()
print("\n")
print(self.team_two.name + " statistics: ")
self.team_two.stats()
print("\n")

team_kills = 0
team_deaths = 0
for hero in self.team_one.heroes:
    team_kills += hero.kills
    team_deaths += hero.deaths
if team_deaths == 0: 
    team_deaths = 1
print9self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

for hero in self.team_one.heroes: 
    if hero.deaths == 0:
        print("survived from " + self.team_one.name + hero.name)

if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        area.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        
        else 
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
        
         
       