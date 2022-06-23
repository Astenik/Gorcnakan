# fahrenheit = (9*celsius + 160) / 5
# Celsius = (fahrenheit - 32) * (5 / 9)
lst = [None] * 11
for i in range(11):
     k = (90*i + 160) / 5
     lst[i] = [i*10, k]

print(f'the list of fahrenheit and celsus from 0 celsus to 100 is: {lst}')
