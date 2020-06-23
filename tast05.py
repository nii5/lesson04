from functools import reduce

def my_multiplication(num1, num2):
    return num1 * num2

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_multiplication, my_list))
