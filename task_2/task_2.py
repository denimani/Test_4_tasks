import math
import argparse


def parse_arguments():
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('circle_info', type=str)
    parser.add_argument('coordinate_points', type=str)
    return parser.parse_args()


def read_circle_info(filename):
    """
    Чтение данных о круге из файла
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        radius = int(lines[1])
        x, y = map(int, lines[0].split())
        return radius, [x, y]


def read_coordinate_points(filename):
    """
    Чтение координат точек из файла
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        points = []
        for line in lines:
            x, y = map(int, line.split())
            points.append((x, y))
        return points


def point_in_circle(center_circle, radius, point):
    """
    Проверка, находится ли точка внутри, на границе или снаружи круга.
    """
    distance = math.sqrt((point[0] - center_circle[0]) ** 2 + (point[1] - center_circle[1]) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    args = parse_arguments()  # разбор аргументов командной строки
    radius, center_circle = read_circle_info(args.circle_info)  # чтение информации о круге
    points = read_coordinate_points(args.coordinate_points)  # чтение координат точек

    # проверка каждой точки и вывод результата
    for point in points:
        print(point_in_circle(center_circle, radius, point))


if __name__ == '__main__':
    main()
