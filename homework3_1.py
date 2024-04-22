from datetime import datetime


def get_days_from_today(date):
    convert_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    different = convert_date.date() - today.date()
    return different


print(get_days_from_today("2024-09-09"))
