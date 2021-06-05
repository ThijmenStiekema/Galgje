#woorden waar die kunnen worden gekozen
words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

#import random module package 
import random


print("hallo".find("l"))

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
    print("Al gekozen letters:") 
    print(*al_gekozen_letters)

    gekozen_letter = input("kies een letter: ")
    if gekozen_letter in al_gekozen_letters:
      print("Letter is al gekozen")
      kiezen()

    elif gekozen_letter.lower() in woord and gekozen_letter.isalpha():
      al_gekozen_letters.append(gekozen_letter)

      #Geeft de locatie van de letters in het woord aan
      index = 0
      while index < len(woord):
        index = woord.find(gekozen_letter, index)
        if index == -1:
            break
        print(index)
        index += 1
      print("Goed gedaan!")
      kiezen()

    elif gekozen_letter.isalpha():
      al_gekozen_letters.append(gekozen_letter)
      print("Fout")
      fouten += 1
      kiezen() 
  
    else: 
      print ("Antwoord is niet een letter of woord")
      kiezen()

def game():
  global woord
  #Kiest woord en zet streepjes neer
  woord = random.choice(words)
  lengte = len(woord)
  print("_ " * lengte)
  global al_gekozen_letters
  al_gekozen_letters = []
  
  kiezen()
  
game()
#Start de game

