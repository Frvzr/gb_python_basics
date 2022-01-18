# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек. 


def convert_time(duration: int) -> str:
    if duration < 60:
        return f'{duration} сек'
    elif duration >= 60 and duration < 3600:
        return f'{duration // 60} мин {duration % 60} сек'
    elif duration >= 3600 and duration < 86400:
        hour = duration // 3600
        minute = (duration % 3600) // 60
        second = (duration % 3600) % 60
        return f'{hour} час {minute} мин {second} сек'
    else:
        day = duration // 86400
        hour = (duration % 86400) // 3600
        minute = ((duration % 86400) % 3600) // 60
        second = ((duration % 86400) % 3600) % 60
        return f'{day} дн {hour} час {minute} мин {second} сек'


duration = 500000
result = convert_time(duration)
print(result)