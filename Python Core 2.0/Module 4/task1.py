from decimal import Decimal
from functools import reduce

def total_salary(path):
    try:
        lines = []
        with open(path, 'r') as filehandler:
            lines = [line for line in filehandler.readlines() if line] # тільки непорожні рядки
        # не тримати файл відкритим під час подальшої обробки даних
        if not len(lines):
            return 0, 0
        salaries = [Decimal(line.split(',')[-1]) for line in lines]
        total = reduce(lambda a, b: a + b, salaries, 0)
        average = total / len(salaries)
        return total, average
    except Exception as e:
        print('An error occured', e)
        return 0, 0

def main():
    total, average = total_salary("employee_salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()