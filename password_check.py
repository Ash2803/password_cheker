print("Введите пароль:")
password = input()
score = 0


def is_very_long():
    if len(password) < 12:
        return False
    return True


def has_digit():
    for element in password:
        if element.isdigit():
            return True
    return False


def has_letters():
    for element in password:
        if element.isalpha():
            return True
    return False


def has_upper_letters():
    for element in password:
        if element.isupper():
            return True
    return False


def has_lower_letters():
    for element in password:
        if element.islower():
            return True
    return False


def has_symbols():
    for element in password:
        if element.isdigit() and element.isalpha():
            return False
    return True


score_count = [
    is_very_long(),
    has_digit(),
    has_letters(),
    has_upper_letters(),
    has_lower_letters(),
    has_symbols()
]

for el in score_count:
    if el is True:
        score += 2

print("Рейтинг пароля: " + str(score))
