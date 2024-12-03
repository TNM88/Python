class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")


class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")


class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        super().display()
        print(f"Passing Year: {self.passing_year}")


class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        super().display()
        print(f"Current Semester: {self.current_semester}")


class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")


if __name__ == "__main__":
    person = Person("Mohammad", "Rahman")
    student = Student("Ayesha", "Siddiqua", 2025)
    alumni = Alumni("Fahim", "Hossain", 2020, 2021)
    current_student = CurrentStudent("Rifat", "Chowdhury", 2024, "6th")
    teacher = Teacher("Anika", "Kabir", 2015)
    admin = Admin("Tanvir", "Ahmed", 2010)
    employee = Employee("Saiful", "Islam", "BD12345")

    print("Person:")
    person.display()
    print("\nStudent:")
    student.display()
    print("\nAlumni:")
    alumni.display()
    print("\nCurrent Student:")
    current_student.display()
    print("\nTeacher:")
    teacher.display()
    print("\nAdmin:")
    admin.display()
    print("\nEmployee:")
    employee.display()
