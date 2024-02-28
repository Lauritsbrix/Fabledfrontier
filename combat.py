import random
from random import randint
from character import character
from stats import stats
import settings
settings.init()

pers = character("player", "halo", "human", "mage")

orcStats = stats (5)
orc = character("enemy", "orc", "orc", "warrior", orcStats)

def main(player, enemy):
    playerHealth = player.stats.health
    enemyHealth = enemy.stats.health
    print(f"player has {playerHealth}, enemy has {enemyHealth}")
    while player.isAlive and enemy.isAlive:
        attack(player, enemy)
        

print("an awesome battle is about to start")
    


def attack(attacker, deffender): 
    print(f"orc has {deffender.stats.health} hp")
    damage = attacker.stats.strength
    deffender.stats.health -= damage
    print(f"orc has {deffender.stats.health} hp")
    
        





attack(pers, orc)
main(pers, orc)






