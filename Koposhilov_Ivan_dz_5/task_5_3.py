from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def check_gen(tutors: list, classes: list):
    """
    Генератор, возвращаюший, значения из двух списков
    """
    # первый вариант с использованием zip
    # while len(tutors) != len(classes):
    #     if len(tutors) > len(classes):
    #         classes.append(None)
    #     else:
    #         tutors.append(None)
    # tutors_class = (idx for idx in zip(tutors, classes))

    # второй вариант zip_longest из itertools
    tutors_class = (idx for idx in zip_longest(tutors, classes, fillvalue=None))
    return tutors_class


generator = check_gen(tutors, classes)
# добавьте здесь доказательство, что создали именно генератор 
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
