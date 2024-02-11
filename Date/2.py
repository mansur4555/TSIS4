from datetime import date, timedelta

bugin = date.today()
erten = bugin + timedelta(1)
keshe = bugin - timedelta(1)

print(bugin.strftime("%A"))
print(erten.strftime("%a"))
print(keshe.strftime("%w"))


print("Today:", bugin)
print("Yesterday:", keshe)
print("Tomorrow:", erten)