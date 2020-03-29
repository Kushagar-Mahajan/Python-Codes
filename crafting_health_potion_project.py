#crafting health potion game

#here we are going to use variable and numbers for it's working
#python random module to create python random generator

import random #imports random module in python

health = 50
print("Health before potion",health) #result before health potion
 
#Easy mode difficulity code

difficulty_1 = 1

potion_health_1 = random.randint(25,50)/difficulty_1 #gives interger value only in this module and divison is used to decrease value of health potion with increasing difficulity
health_1 = health + potion_health_1 
print("Health after potion at easy mode",int(health_1)) #result after health potion  


#Medium mode difficulity code

difficulty_2 = 2

potion_health_2 = random.randint(25,50)/difficulty_2 #gives interger value only in this module and divison is used to decrease value of health potion with increasing difficulity
health_2 = health + potion_health_2
print("Health after potion at easy mode",int(health_2)) #result after health potion  


#Hard mode difficulity code

difficulty_3 = 3

potion_health_3 = random.randint(25,50)/difficulty_3 #gives interger value only in this module and divison is used to decrease value of health potion with increasing difficulity
health_3 = health + potion_health_3
print("Health after potion at easy mode",int(health_3)) #result after health potion  