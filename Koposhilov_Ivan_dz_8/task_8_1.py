import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>[a-zA-Z0-9._-]*[a-zA-Z0-9])+@(?P<domain>[A-Za-z0-9_-]+\.[A-Za-z.]+)')
    #RE_MAIL = re.compile(r'([\w._-]*[\w])+@(\w+\.+\w+)') #Что тут не хватает? Если два домена разбивает на ['', 'ivan.kop', 'somecompany.co', '.ru']
    msg = f'wrong email: {email}'

    if re.match(RE_MAIL, email.strip()):
        valid_email = re.search(RE_MAIL, email)
        print(valid_email.groupdict())
    else:
        raise ValueError(msg)


if __name__ == '__main__':
    email_parse(' someone@geekbrains.ru ')
    email_parse('ivan.kop@some-company.co.ru')
    email_parse('so_m-e.on-e99@geekbrains.ru')
    email_parse('so-me1one@geekbrains.ru')
    email_parse('someone@.geekbrains.ru')
    email_parse('someone@geekbrainsru')