class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"This is {self.name}, a wizard."

# the Student class inherits now the name attribute from the Wizard class
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) # call the init function from the superclass
        self.house = house
    def __str__(self):
        return f"This is {self.name}, a student."


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return f"This is {self.name}, a professor."

# now we can create objects of every class
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence against the dark arts")

print(wizard)
print(student)
print(professor)
