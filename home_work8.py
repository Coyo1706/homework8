import datetime as dt
import dateparser


birthday_per_week = {}

users = [{'Nikola Tesla': '1856/12/10'},
         {'Albert Einstein': '1879.12.11'},
         {'Alain Aspect': '1947,12,15'},
         {'Maryna Viazovska': '02-12-1984'},
         {'Mr. Incognito': '16 Dec 2000'},
         {'Mr. X': '1999 12 17'},
         {'Mr. y': '1999 12 14'}
         ]

users = {k: v for d in users for k, v in d.items()}
users = {k: dateparser.parse(v) for k, v in users.items()}
users = {k: v.replace(year=dt.date.today().year) for k, v in users.items()}

current_date = dt.datetime.today()

while current_date.weekday() < 5:
    current_date = current_date + dt.timedelta(days=1)
if current_date.weekday() == 6:
    current_date = current_date - dt.timedelta(days=1)

end_week = current_date + dt.timedelta(days=6)
print(current_date, end_week)

for name, date in users.items():
    if current_date <= date <= end_week:
        if date.weekday() == 5:
            date = date + dt.timedelta(days=2)
            birthday_per_week[date.strftime('%A')] = name

        if date.weekday() == 6:
            date = date + dt.timedelta(days=1)
            birthday_per_week[date.strftime('%A')] = name
        else:
            birthday_per_week[date.strftime('%A')] = name
print(birthday_per_week)


