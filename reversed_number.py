num = int(input("insert the number: "))   
rev_num = 0
while num != 0:
       rev_num *= 10
       rev_num += num % 10
       num = num // 10

print(f'the revers number is equal to: {rev_num}')
