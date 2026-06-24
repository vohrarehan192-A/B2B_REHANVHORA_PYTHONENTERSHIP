class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create object
student1 = Student("John", 85)

# Call the method
student1.display_details()