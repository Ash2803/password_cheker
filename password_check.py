print("Введите пароль:")
password = input()
score = 0


def is_very_long(password):
    if len(password) < 12:
        return False
    return True


def has_digit(password):
    for el in password:
        if el.isdigit():
            return True
    return False


def has_letters(password):
    for el in password:
        if el.isalpha():
            return True
    return False


def password_score(score):
    if is_very_long(password):
        score += 2
    if has_digit(password):
        score += 2
    if has_letters(password):
        score += 2
    return score


print("Рейтинг пароля: " + str(password_score(score)))
