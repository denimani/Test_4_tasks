import argparse
import json


def parse_arguments():
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('report', type=str)
    parser.add_argument('tests', type=str)
    parser.add_argument('values', type=str)
    return parser.parse_args()


def read_tests_file(filename):
    """
    Метод чтения тестового файла tests.json
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def read_values_file(filename):
    """
    Метод чтения файла с данными values.json
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def form_data_for_report(tests, values):
    """
    Формирование данных для записи в report.json
    """
    for value in values:
        for test in tests:
            if value["id"] == test["id"]:
                test["value"] = value["value"]
            if test.get("values"):
                form_data_for_report(test["values"], values)

    return tests


def write_report_file(filename, data):
    """
    Запись данных в report.json
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    # парсинг аргументов командной строки
    args = parse_arguments()
    # чтение тестового и значения файла
    tests = read_tests_file(args.tests)
    values = read_values_file(args.values)

    # формирование данных для записи в report.json
    data = form_data_for_report(tests['tests'], values['values'])

    # запись данных в report.json
    write_report_file(args.report, data)


if __name__ == '__main__':
    main()
