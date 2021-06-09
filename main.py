#woorden waar die kunnen worden gekozen
words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

#Dingen voor console clearen
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Lijst met tekeningetjes van galgjes
Galgjes = [
  " \n\n\n\n\n", 
  " \n\n\n\n\n_______", 
  "\n| \n| \n| \n| \n|______", 
  "____ \n|   | \n|    \n|    \n|      \n|______", 
  "____ \n|   | \n|   o \n|    \n|      \n|______", 
  "____ \n|   | \n|   o \n|   | \n|      \n|______",
  "____ \n|   | \n|   o \n|  /| \n|      \n|______",
  "____ \n|   | \n|   o \n|  /|\ \n|      \n|______",
  "____ \n|   | \n|   o \n|  /|\ \n|    \n|______",
  "____ \n|   | \n|   o \n|  /|\ \n|  /  \n|______", 
  "____ \n|   | \n|   o \n|  /|\ \n|  / \  \n|______"]

#import random module package 
import random

goede_letters = 0
fouten = 0 

def game():
  #Lost problemen op
  global goede_letters
  global woord
  global lengte
  global gecodeerd_woord
  global al_gekozen_letters
  

  #Zet belangrijke variable en lijsten (terug) naar 0
  goede_letters = 0
  al_gekozen_letters = []
  
  #Kiest woord
  woord = random.choice(words)
  lengte = len(woord)
  
  #Zet streepjes neer
  gecodeerd_woord = ["_ "] * lengte
  kiezen()

def kiezen():
  global fouten

  #Print de tekeningetjes van het galgje gebaseerd op hoeveel fouten er zijn
  print(Galgjes[fouten])
  print()

  #Zet gecodeerd woord neer
  print(*gecodeerd_woord)

  #Checkt of de speler te veel fouten heeft en eindigd de game als dit zo is
  if fouten == 10:
    fouten = 0
    print("Game Over")
    print("Het woord was: " + woord + "\n")
    einde()

  else:
    #Print gekozen letters en zet ze op alphabetische volgoorde
    print("Al gekozen letters of woorden:") 
    al_gekozen_letters.sort()
    print(*al_gekozen_letters)

    #Print hoeveel fouten er zijn gemaakt
    print("fouten: "+ str(fouten))

    #Print hoeveel beurten de speler nog heeft
    aantal_beurten = 10 - fouten
    print("aantal beurten over: " + str(aantal_beurten))

    #Speler kiest letter of woord
    basic_gekozen_letter = input("kies een letter of woord: ")
    gekozen_letter = basic_gekozen_letter.lower()

    #Als de speler al een woord heeft gekozen word dat geblokeerd
    if gekozen_letter in al_gekozen_letters:
      cls()
      print("Letter is al gekozen \n")
      kiezen()

    #De speler wint als hij het woord invult
    elif gekozen_letter == woord:
      print("je hebt het geraden! Het woord was: " + woord)
      print()
      einde()

    #De speler krijgt een punt als hij een letter raad
    elif gekozen_letter in woord and gekozen_letter.isalpha():
      al_gekozen_letters.append(gekozen_letter)
      cls()
      print("Goed gedaan\n")
      #Geeft de locatie van de letters in het woord aan
      index = 0
      while index < len(woord):
        index = woord.find(gekozen_letter, index)
        if index == -1:
          break
        index += 1
        gecodeerd_woord[index-1] = gekozen_letter

      #Laat de speler winnen als alle letters zijn geraden
      if gecodeerd_woord.count("_ ") == 0:
        print("je hebt het geraden! Het woord was: " + woord)
        print()
        einde()
      else:
        kiezen()
    
    elif gekozen_letter.isalpha():
      #voegt een fout toe als de gekozen letter fout is
      al_gekozen_letters.append(gekozen_letter)
      cls()
      print("Fout \n")
      fouten += 1
      kiezen()

    #Blokeert antwoorden die geen letters zijn
    else: 
      cls()
      print ("Antwoord is niet een letter of woord\n")
      kiezen()

def einde():
  #vraagt of de speler wil doorspelen
 doorgaan = input("Wil je nog een keer? (y/n): ")
 if doorgaan == "y":
   doorgaan = 0
   print()
   cls()
   game()
  
 elif doorgaan == "n":
   print("\nBedankt voor het spelen!")
   #Zorgt ervoor dat als de speler niet y of n invoert dat hij het nog een keer kan proberen
  
 else:
    doorgaan = 0
    print("\nVoer y in als je door wil spelen en n in als je wilt stoppen\n")
    einde()

#Start de game
game()