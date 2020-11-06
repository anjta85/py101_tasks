print ('Приветствую друг!')
import random
 
number = random.randint(1, 1000000)
 
while True:
    answer = input('Угадай число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введи число")
        continue

    answer = int(answer)

    if answer < 1 or answer > 1000000:
        print("Число не входит в обозначенный в условии диапазон")
        continue

    if answer == number:
        print('Верно!')
        break
 
    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')