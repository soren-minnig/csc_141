import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    # Creating an instance to use in both test functions
    first_name = 'John'
    last_name = 'Doe'
    annual_salary = 75000
    employee_instance = Employee(first_name, last_name, annual_salary)
    return employee_instance

def test_give_default_raise(employee_instance):
    # Testing the defaul raise
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 80000

def test_give_custom_raise(employee_instance):
    # Testing a custom raise
    employee_instance.give_raise(raise_amount=10000)
    assert employee_instance.annual_salary == 85000