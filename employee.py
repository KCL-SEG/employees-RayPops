"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
#super class of monthly employee and hourly
class Monthly_Employee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        self.salaryType = 'monthly'

    def get_pay(self):
        return self.salary
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}.'
    
class Hourly_Employee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.salaryType = 'hourly'
    
    def get_pay(self):
        return self.hours * self.rate
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.  Their total pay is {self.get_pay()}.'

#classes than inherit contract type, but with added bonus commission functionality
class Bonus_Monthly_Employee(Monthly_Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'
    
class Bonus_Hourly_Employee(Hourly_Employee):
    def __init__(self, name, hours, rate, bonus):
        super().__init__(name, hours, rate)
        self.bonus = bonus

    def get_pay(self):
        return (self.hours * self.rate) + self.bonus
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'

#classes that inherit contract type, but with added contract commision functionality
class Contract_Commission_Monthly_Employee(Monthly_Employee):
    def __init__(self, name, salary, commission, numContracts):
        super().__init__(name, salary)
        self.commission = commission
        self.numContracts = numContracts

    def get_pay(self):
        return self.salary + (self.commission * self.numContracts)
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numContracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'
    
class Contract_Commission_Hourly_Employee(Hourly_Employee):
    def __init__(self, name, hours, rate, commission, numContracts):
        super().__init__(name, hours, rate)
        self.commission = commission
        self.numContracts = numContracts

    def get_pay(self):
        return (self.hours * self.rate) + (self.commission * self.numContracts)
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.numContracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Monthly_Employee('Billie', 4000)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Contract_Commission_Monthly_Employee('Renee', 3000, 200, 4)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Bonus_Monthly_Employee('Robbie', 2000, 1500)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 100, 25)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Contract_Commission_Hourly_Employee('Jan', 150, 25, 220, 3)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Bonus_Hourly_Employee('Ariel', 120, 30, 600)
