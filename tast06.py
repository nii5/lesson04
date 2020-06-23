from itertools import count, cycle

my_list = []
for i in count(start=3, step=1):
    my_list.append(i)
    if i >= 10:
        break
my_sum = 0
for el in cycle(my_list):
    my_sum += el
    if my_sum >= 857:
        break

print(my_sum)
