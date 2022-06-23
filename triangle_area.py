# first option
high = float(input("insert the high of your triangle: "))
base = float(input("insert the base of your triangle: "))
area = (high * base) / 2
print(f'area of your triangle is equal to: {area}')

# second option
s1 = float(input("insert the firs side of your triangle: "))
s2 = float(input("insert the second side of your triangle: "))
s3 = float(input("insert the thired side of your triangle: "))
perimetre = s1 + s2 + s3
s = perimetre / 2 
area2 = (s*(s - s1)*(s - s2)*(s - s3))**(1/2) 
print(f'area of your triangle is equal to: {area2}')
