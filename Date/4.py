from datetime import datetime

bugin = datetime.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
birkun = datetime.strptime('10.02.2028', '%d.%m.%Y')
def difference(dt1, dt2):
    timedelta = dt1 - dt2
    return timedelta.days * 24 * 3600
print(difference(bugin, birkun))