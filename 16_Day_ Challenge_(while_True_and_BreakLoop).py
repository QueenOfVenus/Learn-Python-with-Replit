# ////////////////////////////// While True Loop On Python ///////////////////////////////////

while True:
  print("This program is running")
#  break                                                  break eklemediysek sonsuz döngü başlar.
print("Aww, I was having a good time 😭")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")

# //////Fix The Code//////

counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ")
if addAnother == "no":
  break
print("Bye!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while true:
  color = input("Enter a color: ")
  if color = "red":
  break
  else:
    print("Cool color!")
print("I don't like red")

# //////////// My Code ///////////////

print("Song completion game")
print()
print()

count = 1
while True :
  songWord = input("Oh, the misery! Everybody wants to be my _______ .  ")
  if (songWord == "enemy") :
    break
  else :
    print("Dude, are you sure you know this song? 🤭")
    count += 1
print("Yeah man! We are Imagine Dragons soldiers 💪")
print("You managed to find it on the" , count , ". try")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()
counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")
print("You got the correct lyrics in", counter, "attempt(s).")

# ///////////////// Day 16 Finish /////////////////
