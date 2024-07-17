students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# use a set to get all differnet houses, in sets no element can be more often in the set than once
houses = set()

for student in students:
        houses.add(student["house"])

for house in sorted(houses):
    print(house)
