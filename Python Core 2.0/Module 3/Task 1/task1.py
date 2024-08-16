import datetime
import re

# окрема функція для перетворення рядка на дату
def parse_date(date: str) -> datetime:
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        return None

def get_days_from_today(date: str) -> int:
    parsed_date = parse_date(date)
    if not parsed_date:
        print('Дата введена некоректно')
        return None
    today_date = datetime.date.today()
    difference = parsed_date.date() - today_date
    return difference.days

def main():
    print('Введіть дату в форматі РРРР-ММ-ДД:')
    input_string = input()
    diff = get_days_from_today(input_string)
    if diff is None:
        return
    if diff > 0:
        print(f'Від сьогодні до {input_string} — {diff} днів')
    elif diff < 0:
        print(f'Від {input_string} до сьогодні — {-diff} днів')
    else:
        print(f'{input_string} — це сьогодні')

if __name__ == "__main__":
    main()