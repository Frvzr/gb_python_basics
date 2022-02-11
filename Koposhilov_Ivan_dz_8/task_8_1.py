import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    
    RE_MAIL = re.compile(r'([a-zA-Z0-9.-_$]*[a-zA-Z0-9])+@([A-Za-z0-9]+\.[A-Za-z.]+)')
    #RE_MAIL = re.compile(r'([\w._-]*[\w])+@(\w+\.+\w+)') #если два домена разбивает на ['', 'ivan.kop', 'somecompany.co', '.ru']
    msg = f'wrong email: {email}'
    email_dict = {}

    if re.match(RE_MAIL, email):
        email_list = re.split(RE_MAIL, email)
        email_dict['username'] = email_list[1]
        email_dict['domain'] = email_list[2]
        print(email_dict)
    else:
        raise ValueError(msg)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('ivan.kop@somecompany.co.ru')
    email_parse('someone99@geekbrains.ru')
    email_parse('some1one@geekbrains.ru')
    email_parse('someone@geekbrainsru')