import random

class Hat:
    # house as a class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        #choose a house randomly
        house = random.choice(cls.houses)
        print(name, "is in", house)

Hat.sort("Harry")
