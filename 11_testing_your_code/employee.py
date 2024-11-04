class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_amount=5000):
        # The default is 5000, but a different amount can be given
        self.annual_salary += raise_amount