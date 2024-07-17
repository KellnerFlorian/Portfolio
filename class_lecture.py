# beginn to create a class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # what to print, when one object of the class is being printed out
    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter function for name property, just returning the value of the name
    @property
    def name(self):
        return self._name

    # setter function with error checking, is always calledm if .name is being used
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter function for house property only returning the value of house
    @property
    def house(self):
        return self._house

    #setter function with error checking , is always calledm if .house is being used
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # initializing a student and returning it
    return Student(name, house)

if __name__ == "__main__":
    main()
