import random

def generate_numbers():
    main_numbers = random.sample(range(1, 50), 5)
    bonus_numbers = random.sample(range(1, 10), 2)
    return main_numbers, bonus_numbers

main_numbers, bonus_numbers = generate_numbers()
print("Wylosowane liczby:", main_numbers, bonus_numbers)