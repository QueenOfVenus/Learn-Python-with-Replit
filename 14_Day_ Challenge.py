# ////////////////////////////// Rock , Paper , Scissor Game Application On Python ///////////////////////////////////

from getpass import getpass as input           # Cevapları görünmez yüklüyor. Yazdığında yazılmamış gibi gösteriyor böylece 2 oyuncu da birbirinin cevabını görmüyor. Adil bir kapışma!

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()

if player1Move=="R":
  if player2Move=="R":
    print("You both picked Rock, draw!")
  elif player2Move=="S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2Move=="P":
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="P":
  if player2Move=="R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2Move=="S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player2Move=="P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="S":
  if player2Move=="R":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player2Move=="S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player2Move=="P":
    print("Player1's Scissors make confetti out of Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")

# //////////// My Code ///////////////

from getpass import getpass as input

print("Battle of the Legends - Rock , Paper , Scissor")
print()
print("Welcome everyone to the great fight!")
print("On the right is the champion of years 'PLAYER 1'.")
print("When we look to the left side, we see a new but determined name. 'PLAYER 2'!!!")
print()


player1 = input("Player 1 : R ,P ,S ?  ")
print()
player2 = input("Player 2 : R ,P ,S ?  ")

print()
print("And we have received the match results, dear sports fans.!")
print()

if player1 == "R" :
  if player2 == "R" :
    print("😲 🗿 - 🗿 😲")
  elif player2 == "P" :
    print("🤯 🗿 - 🧻 😎")
  elif player2 == "S" :
    print("🥳 🗿 - ✂️ 😱")
  else :
    print("There is a match fix.!!! ")

if player1 == "P" :
  if player2 == "R" :
    print("🤪 🧻 - 🗿 🤬")
  elif player2 == "P" :
    print("😒 🧻 - 🧻 😒")
  elif player2 == "S" :
    print("😭 🧻 - ✂️ 🤩")
  else :
    print("There is a match fix.!!! ")

if player1 == "S" :
  if player2 == "R" :
    print("🥺 ✂️ - 🗿 😂")
  elif player2 == "P" :
    print("💪😁 ✂️ - 🧻 🤕")
  elif player2 == "S" :
    print("😅 ✂️ - ✂️ 😅")
  else :
    print("There is a match fix.!!! ")


# ///////////////// Day 14 Finish /////////////////
