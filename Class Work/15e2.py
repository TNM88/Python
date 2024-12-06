class SalaryNotInRange(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary < 10000 or salary > 50000:
            raise SalaryNotInRange("Salary is not in the valid range (10,000 - 50,000).")
        self.salary = salary

    def display_salary(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

try:
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))
    emp = Employee(name, salary)
    emp.display_salary()
except SalaryNotInRange as e:
    print(e)
