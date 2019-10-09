"""
Regular Class automatically pass the instance as the first argument and we call that "Self"
Class Method automatically pass the Class as the first Argument and we call that "CLS"
Static Method don't pass anything automatically and they don't pass instances and or the class"""

class Employee:

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, firstname, lastname, pay):
        self.fname = firstname
        self.lname = lastname
        self.pay = pay
        self.mail = self.fname + "." + self.lname + "@gmail.com"

        # as self is meaningless bcz employees number changes for all the employees instances created
        Employee.num_of_emp += 1
    
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def apply_raise_at(self):
        self.pay = int(self.pay * self.raise_amount)

    # using classmethods to change class variables
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # using classmethods as alternative constructors:
    # say someone needs to create employees from a str like this John-doe-30000, so parsing etc is different operation
    # before sending it in here to create so we need a seperate constructor hence
    @classmethod
    def create_employee_from_str(cls, emp_string):
        fname, lname, pay = emp_string.split("-")
        return cls(fname, lname, pay)

    # using staticmethod which doesnt accept instance (self) or class (cls) automatically
    # usually used when your function never is actually using any of the instance or class variables etc like below
    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:  # day.weekday gives numbers for each starting at 1 for monday and endign 6 for sunday
            print("Its a holiday!!!")
            return True
        print("its a working day...")
        return False


emp1 = Employee("karthik", "cey", 20000)
emp2 = Employee("revathi", "mv", 40000)

# so using classmethod to change the class variable like
Employee.set_raise_amt(1.05)  # this is same as Employee.raise_amount = 1.05
print(emp1.pay)
emp1.apply_raise_at()
print(emp1.pay)

# using classmethods as alternative contructors
emp1_str = "Rahul-pg-50000"
new_emp3 = Employee.create_employee_from_str(emp1_str)
print(new_emp3.mail)
print(new_emp3.pay)

# using saticmethod to check if the day is working 
import datetime
my_date = datetime.date(1988, 9, 3)
print(Employee.is_working(my_date))
print(new_emp3.is_working(my_date))
