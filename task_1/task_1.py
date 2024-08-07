import sys


def find_path(n, m):
    # создаем исходный список, где числа от 1 до n повторяются m раз
    list_1 = m * [int(i) for i in range(1, n + 1)]
    list_2 = [' ']  # временный список для хранения текущей последовательности
    list_3 = []  # итоговый список для хранения всех последовательностей
    count = 0  # счетчик для управления смещением

    # выполняем цикл, пока последний элемент временного списка не станет равным 1
    while list_2[-1] != 1:
        list_2.clear()

        for j in range(count, m + count):
            list_2.append(list_1[j])
            count += 1

        list_2_copy = list_2.copy()
        list_3.append(list_2_copy)
        count -= 1

    return list_3


def main():
    # n, m = map(int, input().split())
    # проверяем, что передано достаточно аргументов
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        res = find_path(n, m)

        # выводим первый элемент каждого вложенного списка
        for k in range(len(res)):
            print(res[k][0], end='')


if __name__ == '__main__':
    main()
