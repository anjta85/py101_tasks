"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_or_odd(a):
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_keyword(string):
    return print(keyword.iskeyword(string) or keyword.issoftkeyword(string))


is_keyword("False")

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(obj):
    if isinstance(obj, bool):
        print("Это это логическое выражение")
        return None

    elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
        print("Это число")
        return None

    elif isinstance(obj, str):
        print("Это строка")
        return None

    elif isinstance(obj, NoneType):
        print("Это NoneType")
        return None

    elif isinstance(obj, list):
        print("Это список")
        return None

    elif isinstance(obj, tuple):
        print("Это кортеж")
        return None

    elif isinstance(obj, set):
        print("Это множество")
        return None

    elif isinstance(obj, dict):
        print("Это словарь")
        return None

    else:
        print("Это что-то непонятное")
        return None