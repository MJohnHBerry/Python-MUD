# Abel's notes
# Index:
# 1. 79
# 2. 117
# 3. 141
import time, math, random


#---------------------------------------------------------------#
#                           Classes                            
#---------------------------------------------------------------#
class Entity:
    def __init__ (self, name, attack, defense, speed, hp, max_hp, is_human, first_strike, dead, turn_ended, turn_went):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp
        self.max_hp = max_hp
        self.is_human = is_human
        self.first_strike = first_strike
        self.is_dead = is_dead
        self.turn_ended = turn_ended
        self.turn_went = turn_went 

#---------------------------------------------------------------#
#                           Globals                            
#---------------------------------------------------------------#
COUNT = 0

#---------------------------------------------------------------#
#                           Enemies                            
#---------------------------------------------------------------#
global npc1
npc1 = Entity("Maximus",
                  10,       # Attack
                  5,        # Defense
                  6,        # Speed
                  100,      # HP
                  100,      # Max HP
                  True,    # Is Human Entity bool
                  False,    # Did he win First Strike bool
                  False,    # Is Entity dead bool
                  False,    # Has Turn Ended bool
                  False)    # Has Entity used it's turn bool



#---------------------------------------------------------------#
#                           Character Creation                            
#---------------------------------------------------------------#
def game_intro():
    print("Welcome to the Battle Arena.")
    user_input = input("Your name, gladiator? \n")
    global player1
    player1 = Entity(user_input,
                  10,       # Attack
                  5,        # Defense
                  5,        # Speed
                  100,      # HP
                  100,      # Max HP
                  True,    # Is Human Entity bool
                  False,    # Did he win First Strike bool
                  False,    # Is Entity dead bool
                  False,    # Has Turn Ended bool
                  False)    # Has Entity used it's turn bool
    print("Step forth, ", player1.name, ".")
    print(player1.name, " steps forward onto the sands of blood to face his opponent, ", npc1.name,"...")



#---------------------------------------------------------------#
#                           Actions                            
#---------------------------------------------------------------#
def skill_attack(Attacker, Defender):
    rand = random.randint(1, 5)
    Defender.hp -= Attacker.attack + rand - Defender.defense
    print(Attacker.name, "attacks ", Defender.name, " for ", Attacker.attack + rand - Defender.defense, "points of damage!")
    # Could be a separate function
    # def is_dead()
    if(Defender.hp <= 0):
        print(Attacker.name," has slain ",Defender.name)
    else:
        print(Defender.name, "'s HP is at ", Defender.hp)


def skill_defend(defending):
    defending.defense + 3
    global COUNT
    counter = COUNT
    print(defending.name," raises his shield to defend against the oncoming blow.\nDefense increased by 3 for 1 round.")
    if(COUNT == counter + 2):
        return speedup.defense - 3


def skill_psyche(speedup):
    speedup.speed + 4
    global COUNT
    counter = COUNT
    if(COUNT == counter + 4):
        return speedup.speed - 4


#---------------------------------------------------------------#
#                           Combat                            
#---------------------------------------------------------------#
def turn_counter():
    global COUNT
    COUNT = COUNT + 1
    print("Current combat turn: ", COUNT)


def get_player_combat_choice():
    user_input = input("""
    (A)ttack
    (D)efend
    (P)syche Up
    """)
    if(user_input == "A"):
        skill_attack(Attacker, Defender)
        Attacker.turn_ended = True


    elif(user_input == "D"):
        skill_defend(Attacker)
        Attacker.turn_ended = True

    elif(user_input == "P"):
        skill_psyche(Attacker)
        Attacker.turn_ended = True

    else:
        print("Please choose correctly.")
        speed_check(Attacker, Defender)
            
def npc_combat_choice():
    rand = random.randint(1, 3)
    if rand == 1 :
        skill_attack(Defender, Attacker)
        Defender.turn_ended = True
    elif rand == 2 :
        skill_defend(Defender)
        Defender.turn_ended = True
    else:
        print(Defender.name," psyches himself up.")
        Defender.turn_ended = True

  

def speed_check(Attacker, Defender):
    if(Attacker.speed >= Defender.speed and Attacker.turn_ended == False):
      get_player_combat_choice()
    elif(Attacker.speed <= Defender.speed and Attacker.turn_ended == False):
      get_p
      
def is_dead(entity):
	if(entity.hp <= 0):
    	entity.is_dead = True
        print("You have")
    

    
#---------------------------------------------------------------#
#                           Game Loop                            
#---------------------------------------------------------------#
game_intro()
while(player1.hp > 1 and npc1.hp > 1):
    turn_counter()
    speed_check(player1, npc1)