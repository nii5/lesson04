from sys import argv

def calculation_salary(production, rate, prize=0):
    salary = (int(production) * int(rate)) + int(prize)
    print(salary)

production, rate, prize= argv[1:]

calculation_salary(production, rate, prize)

