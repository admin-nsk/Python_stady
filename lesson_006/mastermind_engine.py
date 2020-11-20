import random

secret_number = ''


def puzzle_number():
    for i in range(4):
        if i == 0:
            number = random.randint(1, 9)
            secret_number = str(number)
        else:
            number = random.randint(0, 9)
            n = 0
            while n != len(secret_number):
                n += 1
                while int(secret_number[n-1]) == number:
                    number = random.randint(0, 9)
                    n = 0
            secret_number += str(number)
    return secret_number


def check_number(secret_number, user_number):
    quantity_cow = 0
    quantity_bulls = 0
    for i in range(4):
        if secret_number[i] == user_number[i]:
            quantity_bulls += 1
        for n in range(4):
            if secret_number[n] == user_number[i]:
                quantity_cow += 1
    result = {'Bulls': quantity_bulls, 'Cow': quantity_cow}
    return result



