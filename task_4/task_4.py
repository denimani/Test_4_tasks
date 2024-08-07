import argparse


def parse_arguments():
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', type=str)
    return parser.parse_args()


def read_numbers_file(filename):
    """
    Чтение файла с числами
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [int(line) for line in file]


def minimal_moves(nums):
    """
    Минимальное количество ходов для упорядоченного массива
    """
    nums.sort()
    len_nums = len(nums)
    mid_index = len_nums // 2

    if len_nums % 2 == 0:
        median = (nums[mid_index - 1] + nums[mid_index]) / 2
    else:
        median = nums[mid_index]

    return sum(abs(num - median) for num in nums)


def main():
    args = parse_arguments()
    nums = read_numbers_file(args.numbers)

    print(minimal_moves(nums))


if __name__ == '__main__':
    main()
