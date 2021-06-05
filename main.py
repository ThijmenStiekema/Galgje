#woorden waar die kunnen worden gekozen
words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

#import random module package 
import random


print("ahllo".find("l"))

fouten = 0

def kiezen():
    #Checkt of de speler game over is en herstart de game
  
  global fouten  
  if fouten == 12:
    fouten = 0
    print("Game Over")
    input("press enter to continue ")
    game()
  
  else:
    gekozen_letter = input("kies een letter: ")
    if gekozen_letter in woord:
      index = 0
      while index < len(woord):
        index = woord.find(gekozen_letter, index)
        if index == -1:
            break
        print(index)
        index += 1

    
      print("Goed gedaan!")
      kiezen()
    else:
      print("Fout")
      fouten += 1
      kiezen() 
      

def game():
  global woord
  #Kiest woord en zet streepjes neer
  woord = random.choice(words)
  lengte = len(woord)
  print("_ "*lengte)

  kiezen()
  
game()
#Start de game

