class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        print("Employee name :",self.name)
    def get_salary(self):
        print("Salary of the employee ",self.name,"is ",self.salary)