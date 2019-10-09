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

    # need sometimes to be done equally for all employees , say hike so
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    # can call the raise_amount as self.raise amount or more correctly employee.raise amount as its class vairable
    # actually raise amount is non existend for the instance like emp1 or emp2 look line 31 but if not there it will
    # look if the class has and then use it
    def apply_raise_at(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("karthik", "cey", 20000)
emp2 = Employee("revathi", "mv", 40000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
# this is good but the variable is constant may need to change
print(emp1.__dict__)
print(Employee.num_of_emp)
