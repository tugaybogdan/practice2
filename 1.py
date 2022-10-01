DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}  
 
def next_date(day, month, year):
    day += 1
    if day > DAYS_IN_MONTH[month]:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return day, month, year

day, month, year = map(
    int,
    input('Введите дату напр.24.09.2022 ->').split('.')
)
print(next_date(day,month, year))