def is_ideal(num:int):
    i = 1 
    sum = 0
    while i <= num // 2:
          if num % i == 0:
              sum += i 
    return True if sum == n else False

n = int(input("insert number: "))
print(is_ideal(n))
