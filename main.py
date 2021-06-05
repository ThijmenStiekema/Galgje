#woorden waar die kunnen worden gekozen
words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

#import random module package 
import random

goede_letters = 0
fouten = 0

def game():
  global goede_letters
  goede_letters = 0
  global woord
  #Kiest woord en zet streepjes neer
  woord = random.choice(words)
  global lengte
  lengte = len(woord)
  global gecodeerd_woord
  gecodeerd_woord = ["_ "] * lengte
  global al_gekozen_letters
  al_gekozen_letters = []
  kiezen()


def kiezen():
  print(*gecodeerd_woord)
  #Checkt of de speler game over is en herstart de game
  global fouten
  if fouten == 12:
    fouten = 0
    print("Game Over")
    input("press enter to continue ")
    game()

  else:
    #print gekozen letters
    print("Al gekozen letters:") 
    print(*al_gekozen_letters)
    print("fouten: "+ str(fouten))
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
        index += 1
        gecodeerd_woord[index-1] = gekozen_letter
      print("Goed gedaan!")
      if gecodeerd_woord.count("_ ") == 0:
        print("GG")
        input("press enter to continue ")
        print(woord)
        game()
      else:
        kiezen()
      
    elif gekozen_letter.isalpha():
      al_gekozen_letters.append(gekozen_letter)
      print("Fout")
      fouten += 1
      kiezen() 
  
    else: 
      print ("Antwoord is niet een letter of woord\n")
      kiezen()

game()
#Start de game
