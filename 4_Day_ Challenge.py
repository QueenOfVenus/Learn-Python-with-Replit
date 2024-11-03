# ////////////////////////////// Colorful Texts On Python ///////////////////////////////////

Default	0
Black	30
Red	31
Green	32
Yellow	33
Blue	34
Purple	35
Cyan	36
White	37

print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")   ///default red default

# //////Fix The Code//////



# //////////// My Code ///////////////

print("Welcome to your adventure simulator. ")
print()
print(" I am going to ask you a bunch of questions and then ")
print("create an epic story with you as the star!")

print()

name = input("What is your name?: ")
enemy = input("What is your worst enemy’s name?: ")
power = input("What is your superpower?: ")
live = input("Where do you live?: ")
food = input("What is your favorite food?: ")

print()

print("Hello ", "\033[35m", name, "\033[0m ! Your ability to ", power, " will make sure you never ")
print(" have to look at ", enemy, " again. Go eat ", food,
      " as you walk down ")
print("the streets of ", live, " and use ", power, " for good and not evil! ")


# ///////////////// Day 4 Finish /////////////////
