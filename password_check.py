import urwid


def is_very_long():
    if len(str(ask)) < 12:
        return False
    return True


def has_digit():
    for element in str(ask):
        if element.isdigit():
            return True
    return False


def has_letters():
    for element in str(ask):
        if element.isalpha():
            return True
    return False


def has_upper_letters():
    for element in str(ask):
        if element.isupper():
            return True
    return False


def has_lower_letters():
    for element in str(ask):
        if element.islower():
            return True
    return False


def has_symbols():
    for element in str(ask):
        if element.isdigit() and element.isalpha():
            return False
    return True


def rating_score():
    score = 0
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
    return score


def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг пароля: %s" % rating_score())


ask = urwid.Edit('Пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
