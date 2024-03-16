
from random import randint
# print(*iter(lambda:randint(0,99),0),0)


random_numbers = []
while True:
    new_random_number = randint(0, 99)
    random_numbers.append(new_random_number)
    if new_random_number == 0:
        break
    

print(random_numbers)
