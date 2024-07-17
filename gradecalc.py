# ask the user for the maximum points there are on the exam
maxPoints = int(input("What is the maximum of points in your exam? "))
print("Here is a possible grade point system")


# calculate the lower bound of points someone has to earn, in order to get a 4, 3, 2, 1
minPointsfor4 = round(maxPoints * 0.5)
minPointsfor3 = round(maxPoints * 0.625)
minPointsfor2 = round(maxPoints * 0.75)
minPointsfor1 = round(maxPoints * 0.875)

# print the concrete gradelist
print("Sehr gut", "ab",  minPointsfor1,  "Punkten")
print("Gut", "ab",  minPointsfor2,  "Punkten")
print("Befriedigend", "ab", minPointsfor3, "Punkten")
print("Genügend", "ab", minPointsfor4, "Punkten")
print("Nicht genügend", "bei weniger als", minPointsfor4, "Punkten")
