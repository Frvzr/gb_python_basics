import re


def nginx_log_parse(logs: str) -> dict:
    """
    Парсит переданную строку с файла с логами
    :param logs: строковое входное значение обрабатываемой строчки лога
    :return: log
    """
    RE_LOGS = re.compile(r'(^[a-f0-9.:]+|\d{2}/[a-zA-Z]{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}|(?<=\")[A-Z]+\b|/[a-z]+/\w+|(?<!\S)\d+(?!\S))')
    log = re.findall(RE_LOGS, logs)
    return tuple(log)


if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(nginx_log_parse(line))