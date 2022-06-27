import urwid


def is_very_long(password):
    return len(str(password)) > 12


def has_digit(password):
    return any(element.isdigit() for element in str(password))


def has_letters(password):
    return any(element.isalpha() for element in str(password))


def has_upper_letters(password):
    return any(element.isupper() for element in str(password))


def has_lower_letters(password):
    return any(element.islower() for element in str(password))


def has_symbols(password):
    return any(not element.isalnum() for element in str(password))


def rating_score(password):
    validators = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    score = 0
    for validator in validators:
        if validator(password):
            score += 2
    return score


def password_rait(edit, new_edit_text):
    reply.set_text("Рейтинг пароля: %s" % rating_score(new_edit_text))


if __name__ == '__main__':
    password = urwid.Edit('Пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', password_rait)
    urwid.MainLoop(menu).run()
