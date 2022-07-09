
# python3 manage.py runscript many_load

import requests
import datetime as dt
from portafolioVirtual.models import Company, Date1, Historic


def run():
    name = input("Tu sabes que hacer")
    END = dt.datetime.now() - dt.timedelta(days= 365 * 10)
    #ZBNR1TO0TXAUB2YT.
    params = {
  'access_key': '9ca16a5226c4fef3f3e73cdae5734de6',
  "symbols": name,
  "offset":0,
  "limit": 1000,
  "date_from": END.date(),
  "date_to": dt.datetime.now().date()

    }

    r = requests.get('http://api.marketstack.com/v1/eod', params)



    data = r.json()

    print(data)

    Company.objects.all().delete()
    Date1.objects.all().delete()
    Historic.objects.all().delete()

    monthly = list()
    temp2 = dict()
    company1 = data["data"][0]["symbol"]
    date_date = dt.datetime.strptime(data["data"][0]["date"], '%Y-%m-%dT%H:%M:%S+0000')
    temp1 = date_date.month
    for day in data["data"]:
        day_time = dt.datetime.strptime(day["date"], '%Y-%m-%dT%H:%M:%S+0000')
        if(day_time.month == temp1):
            temp2[day_time] = day["close"]
        else:
            temp1 = day_time.month
            temp3 = [value for value in temp2.keys()]
            maximo = max(temp3)
            monthly.append((maximo, temp2[maximo]))
            temp2 = dict()
            temp2[day_time] = day["close"]



    for day, price in monthly:
        C, created = Company.objects.get_or_create(name = company1)
        D, created = Date1.objects.get_or_create(name = day)
        r = price
        H = Historic(price=r, company=C, date=D)
        H.save()



