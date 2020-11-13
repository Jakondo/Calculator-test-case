
def multiply(a, b):
    c = a * b
    return c


def sum(a, b):
    c = a + b
    return c


def neg(a, b):
    c = a - b
    return c


def division(a, b):
    c = a/b
    return c

if __name__ == '__main__':
    while True:
        print("Выберите действие: \n1 - Умножение \n2 - Деление \n3 - Сложение \n4 - Вычитание")
        choise = input()

        if choise == "1":
            print("Введите первое число: ")
            first = int(input())
            print("Введите второе число: ")

            sec = int(input())
            end = multiply(first, sec)
            print(end)
        elif choise == "2":
            print("Введите первое число: ")
            first = int(input())
            print("Введите второе число: ")

            end = division(first, sec)
            print(end)
        elif choise == "3":
            print("Введите первое число: ")
            first = int(input())
            print("Введите второе число: ")

            end = sum(first, sec)
            print(end)
        elif choise == "4":
            print("Введите первое число: ")
            first = int(input())
            print("Введите второе число: ")

            end = neg(first, sec)
            print(end)
        elif choise == "q":
            break
