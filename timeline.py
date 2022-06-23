# 1 day = 24 hour
# 1hour = 60 min
# 1 min = 60 sec
day = float(input("insert the  your timeline  days: "))
hour = float(input("insert the  your timeline  hours: "))
min = float(input("insert the  your timeline  hors: "))
sec = float(input("insert the  your timeline  seconds: "))
s = day * 12 * 3600
s1 = hour * 3600
s2 = min * 60
print(f'your timeline with seconds is equal to: {s + s1 + s2 + sec} sec')
