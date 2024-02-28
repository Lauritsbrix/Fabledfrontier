import random
from random import randint
from character import character
from stats import stats
import settings
settings.init()
import time
import os

pers = character("player", "halo", "human", "mage")

orcStats = stats (5)
orc = character("enemy", "orc", "orc", "warrior", orcStats)

def main(player, enemy):
    os.system("cls")
    print("an awesome battle is about to start")
    playerHealth = player.stats.health
    enemyHealth = enemy.stats.health
    print(f"player has {playerHealth}, enemy has {enemyHealth}")
    time.sleep(3)
    while player.isAlive and enemy.isAlive:
        os.system("cls")
        attack(player, enemy)
        playerHealth -=1
        print("Enemy attacks! player health: ",playerHealth)
        enemyHealth -= 1
        print("Player attacks! enemy health: ",enemyHealth)
        
        
        
        if playerHealth <=0:
            player.isAlive = False
            print("You have lost  the combat")
        
        if enemyHealth <=0:
            enemy.isAlive = False
            print("you won the combat")
            print(f"{enemy.name} has been defeateed")

        time.sleep(2)
   
   

        


    


def attack(attacker, deffender): 
    damage = attacker.stats.strength
    deffender.stats.health -= damage
    
    

attack(pers, orc)
main(pers, orc)






