
from datetime import datetime
import random
import re

def get_days_from_today(date:str) -> int:
    """
    This stuff takes any string date, formated like: '%Y-%m-%d',
    and returns difference, as a number of days(int), between them!
    """
    try:
        instance = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        return (instance - today).days
    except ValueError:
        print('Your date does not match format!')


def get_numbers_ticket(min: int, max:int, quantity:int)-> list:
    """
    This returns a list of original numbers from the sequence!
    """
    if min > 0 and max <= 1000:
        sequence = range(min, max+1)
        try:
            sample = random.sample(sequence, quantity)
            return sorted(sample)
        except ValueError:
            print('Quantity is out of range! Please enter correct quantity!')
    else:
        return []


def normalize_phone(phone_number:str) -> str:
    """
    This function transforns phone numbers to the standard form!
    """
    pattern = r'[^0-9\+]'
    replacement = ''
    phone_number = re.sub(pattern, replacement, phone_number)
#expected answer
    if phone_number.startswith('38'):
        phone_number = '+' + phone_number
    elif phone_number.startswith('0'):
        phone_number = '+38' + phone_number
    return phone_number
#alternative realisation
    # phone_number = '+380' + phone_number[-9:]
    # return phone_number




if __name__ == '__main__':
    #test 1
    print('test1')
    print(get_days_from_today("2021-10-09"))

    #test 2
    print('test2')
    lottery_numbers = get_numbers_ticket(1, 10, 100)
    print('Your lottery numbers: ', lottery_numbers)

    #test 3
    print('test3')
    raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
