import datetime as dt

date_string = "2021-09-24T00:00:00+0000"

date_date = dt.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S+0000')
print(date_date.month)