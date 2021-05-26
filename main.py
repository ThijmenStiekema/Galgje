words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]
fouten = 0

#import random module package  
import random

def game():
  woord = random.choice(words)
  lengte = len(woord)
  print("_ "*lengte)

  def kiezen():
    if fouten == 12:
      print("Game Over")
      input("press enter to continue")
      game()
    
    else:
      gekozen_letter = input("kies een letter ")
    
game()
