import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=1, day=7, hour=4)
print(date_of_birth)