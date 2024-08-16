import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # max — включна верхня межа. У викликах буде max+1 — виключна
    # quantity має лежати не між min і max, а між 0 і загальною кількістю розігруваних номерів
    if min < 1 or max > 1000 or quantity < 0 or quantity > max-min+1 or max < min:
        return []
    return sorted(random.sample(range(min, max+1), quantity))

def main():
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

if __name__ == "__main__":
    main()