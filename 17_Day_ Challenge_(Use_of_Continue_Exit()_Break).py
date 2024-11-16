# ////////////////////////////// Continue & Break & Exit() On Python ///////////////////////////////////

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")

# //////Fix The Code//////

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit
print("The game is over, you've failed!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute"
    print("Game over!")
  break
  elif direction == "ladder":
    continue
else:
    print("Game over!")
    exit 
print("Thanks for playing!")

# //////////// My Code ///////////////

from getpass import getpass as input

print("Battle of the Legends - Rock , Paper , Scissor")
print()
print("Welcome everyone to the great fight!")
print("On the right is the champion of years 'PLAYER 1'.")
print("When we look to the left side, we see a new but determined name. 'PLAYER 2'!!!")
print()

round = 0
p1 = 0
p2 = 0


print()
print("And we have received the match results, dear sports fans.!")
print()

while True :
  if round == 5 :
    print("Total Score" , p1 , " - " , p2)
    print ("Game over guys! Come on, go home. Good Night")
    exit()
  else :
    round +=1
    print()
    print("Round " , round , " :")
    print()
    player1 = input("Player 1 : R ,P ,S ?  ").upper()
    print()
    player2 = input("Player 2 : R ,P ,S ?  ").upper()

    if player1 not in ["R","P","S"] or player2 not in ["R","P","S"] :
      print("Match cancellation cheat detected")
      break  # Döngüyü tamamen sonlandırır
      
    if player1 == "R" :
      if player2 == "R" :
        print("😲 🗿 - 🗿 😲")
        continue
      elif player2 == "P" :
        print("🤯 🗿 - 🧻 😎")
        p2 += 1
        continue
      elif player2 == "S" :
        print("🥳 🗿 - ✂️ 😱")
        p1 += 1
        continue

    

    if player1 == "P" :
      if player2 == "R" :
        print("🤪 🧻 - 🗿 🤬")
        p1 += 1
        continue
      elif player2 == "P" :
        print("😒 🧻 - 🧻 😒")
        continue
      elif player2 == "S" :
        print("😭 🧻 - ✂️ 🤩")
        p2 += 1
        continue

    if player1 == "S" :
      if player2 == "R" :
        print("🥺 ✂️ - 🗿 😂")
        p2 += 1
        continue
      elif player2 == "P" :
        print("💪😁 ✂️ - 🧻 🤕")
        p1 += 1
        continue
      elif player2 == "S" :
        print("😅 ✂️ - ✂️ 😅")
        continue


  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        

  from getpass import getpass as input


print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
#hint: create these variables outside loop and then add += with correct player to keep score throughout
player1_score = 0
player2_score = 0
#hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once. 
while True: 
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
  
  if(player1Move=="R"):
    if(player2Move=="R"):
      print("You both picked Rock, draw!")
    elif(player2Move=="S"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="P"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
  
# hint: make sure you add player scores at the end of all the options but still inside the while loop.
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue


# ///////////////// Day 17 Finish /////////////////
