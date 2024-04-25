from datetime import datetime


def get_days_from_today(date):
    convert_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    difference = convert_date.date() - today.date()
    days_difference = difference.days
    return days_difference


print(get_days_from_today("2024-09-09"))
