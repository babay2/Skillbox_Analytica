class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def parseline(line):
    line_split = line[:-1].split(' ')
    if len(line_split) < 3:
        raise ValueError('НЕ присутствуют все три поля')
    elif not 10 <= int(line_split[2]) <= 99:
        raise ValueError('Возраст не в диапазоне')
    elif not '@' in line_split[1] or not '.' in line_split[1]:
        raise NotEmailError('Неправильный формат email')
    for elem in line_split[0]:
        if elem.isdigit():
            raise NotNameError('Имя не должно содержать цифр')
    return line[:-1]


with open('registrations_.txt', 'r', encoding='utf8') as f:
    for line in f:
        try:
            data = parseline(line)
            file = open('registrations_good.log', 'a')
            file.write(data + '\n')
            file.close()
        except Exception as exc:
            file = open('registrations_bad.log', 'a')
            file.write(line)
            file.close()
