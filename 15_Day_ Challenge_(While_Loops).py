# ////////////////////////////// While Loops On Python ///////////////////////////////////

# While Loop
counter = 0
while counter < 10:
  print(counter)
  counter +=1

# Infinite Loop                  deneme sonsuz döngüye girersin
counter = 0
while counter < 10:
  print(counter)
counter +=1



# //////Fix The Code//////

counter = 0
while counter < 10:
  print(counter)


counter = 0
while counter > 6:
  print(counter)
  counter += 1


exit = ""
while exit != "yes":
  print("🥳")
exit = input("Exit?: ")


counter = 0
while counter < 25:
  print(counter)


counter = 0
while counter >= 12:
  print(counter)
  counter += 1


exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ")

# //////////// My Code ///////////////

control = "no"

while (control != "yes") :
  animal = input("Choose your soul animal.!!: ")
  if (animal == "Racoon") :
    print("Yes, they are really cute, oh I would eat them...")
  elif (animal == "Panda") :
    print("Or do you roll on the ground when you're sad too?")
  elif (animal == "Lion") :
    print("Roarrr!")
  else :
    print("Liar! Liar! No one will believe you!! There is no such animal.")
  control = input("Do you want to exit?: ")



exit = "no"


while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")

# ///////////////// Day 15 Finish /////////////////
