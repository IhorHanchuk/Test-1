from random import randint

name = input("Привіт, як вас звуть?: ")
print("{name}, ви попали в гру: 'Вгадай число'.")
num = randint(100, 1000)
rahunok = 0

while True:
    numb = int(input("Виберіль число: "))
    rahunok += 1

    if numb == num:
        print(f"Вітаю, ви вгадали число {num} за {rahunok} спроб.")
        break
    elif numb > num:
        print("Ваше число більше за загадане.")
    elif numb < num:
        print("Ваше число менше за загадане.")

print("Гра завершена.")