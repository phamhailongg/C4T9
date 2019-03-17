class Employee : 
    def __init__(self, first_name, last_name, middle_name, pay) : 
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + last_name + middle_name + "@gmail.com"
        self.pay = pay

em1 = Employee("Long", "Pham","Hai123", 100000)
print(em1.email)
