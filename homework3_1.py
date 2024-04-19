from datetime import datetime


def get_days_from_today(date):
    convert_date = datetime.strptime(date, "%Y-%m-%d")
    #today = datetime.today()
    today = datetime(year=2021, month=5, day=5)
    different = convert_date.date() - today.date()
    return different


print(get_days_from_today("2021-10-09"))