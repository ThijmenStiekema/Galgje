words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]
  
#import random module package  
import random

def game():
  woord = random.choice(words)
  lengte = len(woord)
  print("_ "*lengte)

game()

