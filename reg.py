class Student:
    def __init_(self, name, reg_number, course, year):
        self.name = name
        self.reg_number = reg_number
        self.course = course
        self.year = year

    def __str_(self):
        return(f"name: {self.name} reg_number: {self.reg_number} course: {self.course} year: {self.year}")
    
Student1 = Student("Mukisa Moureen", "M23B13/099", "BSIT", 2024)
Student2 = Student("Kisakye Sandrah", "S23B13/45", "law", 2024)
student3 = Student("mwesigwa james", "M23B13/106", "BSIT", 2024)
student4 = Student("dauglas enock", "M23B13/077", "BSCS", 2024)

print(student3)



