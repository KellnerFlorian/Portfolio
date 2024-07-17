name = input("What's your name? ")

#open a text file an appen ("a") names to it

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

