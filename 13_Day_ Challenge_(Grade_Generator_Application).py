# ////////////////////////////// Grade Generator Application On Python ///////////////////////////////////

print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()



number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score)*100, 2)

print("You got",final_perc,"%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")

# //////////// My Code ///////////////

lessonName = input("Lesson name?  ")
maxGrade = int(input("What is max grade?  "))
yourGrade = int(input("What is your grade?  "))

if (maxGrade * 0.10) >= yourGrade >= (maxGrade * 0.9) :
  print("Marvelous! Congratulations🥳 Your Grade is A+ ")
elif (maxGrade * 0.9) > yourGrade >= (maxGrade * 0.8) :
  print("That's cool! Your Grade is A")
elif (maxGrade*0.8) > yourGrade >= (maxGrade*0.7) :
  print("Not bad, man. Don't be sad, you'll do better next time! Your Grade is B")
elif (maxGrade*0.7) > yourGrade >= (maxGrade*0.6) :
  print("Are you sure you're studying for this exam?! Your Grade is C")
elif (maxGrade*0.6) > yourGrade >= (maxGrade*0.5) :
  print("Bro, you have a lot of shortcomings that you need to close.! Your Grade is D")
elif (maxGrade*0.5) > yourGrade >= (maxGrade*0.0) :
  print("Oh Dude, you're so lazy! Your Grade is U")
else :
  print("Somethings wrong Dude.!")


# ///////////////// Day 13 Finish /////////////////
