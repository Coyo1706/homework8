import datetime as dt
import dateparser
from collections import defaultdict


birthday_per_week = defaultdict(list)

users = [{'Nikola Tesla': '1856/12/10'},{'Albert Einstein': '1879.12.11'}, {'Alain Aspect': '1947,12,15'},
         {'Maryna Viazovska': '12-12-1984'}, {'Mr. Incognito': '16 Dec 2000'},  {'Mr. X': '1999 12 17'},
         {'Mr. Y': '1999 12 14'}, {"Yulia": "06/12/1996"}, {'Yarpl': '07/12/1997'}, {'Sunny': '26/12/2000'},
         {'Luk': '10/12/1995'}, {'Sim': '12/12/1991'}, {'Nok': '14/12/1994'}, {'Kred': '13/12/1994'},
         {'Tim': '18/12/1997'}, {'Kooc': '09/12/1997'}
         ]


users = {k: v for d in users for k, v in d.items()}
users = {k: dateparser.parse(v) for k, v in users.items()}
users = {k: v.replace(year=dt.date.today().year) for k, v in users.items()}

current_date = dt.date.today()

while current_date.weekday() < 5:
    current_date = current_date + dt.timedelta(days=1)
    
if current_date.weekday() == 6:
    current_date = current_date - dt.timedelta(days=1)

end_week = current_date + dt.timedelta(days=6)


for name, dates in users.items():

    if current_date <= dates.date() <= end_week:

        if 0 < dates.weekday() < 5:
            birthday_per_week[dates.strftime('%A')].append(name)

        elif dates.weekday() == 5:
            dates = dates + dt.timedelta(days=2)
            birthday_per_week[dates.strftime('%A')].append(name)

        else:
            dates = dates + dt.timedelta(days=1)
            birthday_per_week[dates.strftime('%A')].append(name)

for k, v in birthday_per_week.items():
    print(k, ":", str(v).replace('[', '').replace(']', '').replace('\'', ''))



