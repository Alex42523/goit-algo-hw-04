import random
from datetime import datetime
def get_days_from_today(date):
    today = datetime.today()
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Невірний тип дати!"
    a = today - date
    return a.days
print(get_days_from_today("2021-109"))
print(get_days_from_today("2021-10-09"))
def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= max <= 1000 and max - min >= quantity:
        numbers = set()
        while len(numbers) < quantity:
            number = random.randint(min, max)
            numbers.add(number)
        return sorted(numbers)
    else:
        return []
print(get_numbers_ticket(10, 20, 10))
print(get_numbers_ticket(10,14,6))
print(get_numbers_ticket(5, 10, 3))