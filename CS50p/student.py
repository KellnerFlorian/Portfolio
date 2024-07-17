# beginn to create a class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # what to print, when one object of the class is being printed out
    def __str__(self):
        return f"{self.name} from {self.house}"

    # means you can call this function without instantiating a object of the class first
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
