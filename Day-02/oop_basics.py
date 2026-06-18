class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
employee1 = Employee("Vijay", 18)
employee1.display_info()
