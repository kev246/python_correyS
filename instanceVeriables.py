class Employee:
    def __init__(self, firstname, lastname, pay):
        self.fname = firstname
        self.lname = lastname
        self.pay = pay
        self.mail = self.fname + "." + self.lname + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)


emp1 = Employee("karthik", "cey", 20000)
emp2 = Employee("revathi", "mv", 40000)

print(emp1.fname)
print(emp2.mail)
print("{} {}".format(emp1.fname, emp1.lname))
# instead of writing as above lets do the functionality within class for creating full name
print(emp2.fullname())

# also can call the function as below but have to pass the instance (this happens in backend while calling with
# instance and that is passed as which makes the requirement of self , so self means passing the instance itself
# which is automatically passed when self is there as parameter)
Employee.fullname(emp1)
