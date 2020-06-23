
def fact(n):
    for i in range(1, n+1):
        yield i

n = 4
factor = 1
for el in fact(n):
    factor *= el

print(f'Факториал {n}! = {factor}')
