# ////////////////////////////// Mathematical Expressions On Python ///////////////////////////////////

adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

# **********************************************

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople

answer = round(answer, 2)         # Bu satırı ondalık sayının virgülden sonra kaç basamağının gözükmesini istiyorsak o sayıyı belirtiyoruz. Round ediyoruz yani yuvarlıyoruz.      

print("You all owe", answer)



# //////Fix The Code//////

👉 # Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
3.4 * 6.8

# division
2467 / 4673

#raise 10 to the power of 2

# print the remainder when 343 is divided by 4
print("343 // 100")

# //////////// My Code ///////////////

# Çözüm 1
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(myBill * 0.2)
print(tip)
addTip = myBill + tip
answer = addTip / numberOfPeople
print("You all owe", answer)


print()
print()

# Çözüm 2

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("How much add tip: 15 - 18 - 20 ?  "))
percent = float(myBill * (tip / 100))
print(percent)
addTip = myBill + percent
answer = addTip / numberOfPeople
print("You all owe", answer)

print()
print()

# Çözüm 3

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)

# ///////////////// Day 10 Finish /////////////////
