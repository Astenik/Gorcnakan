def is_simple(n):
        if n == 1:
            return False
        i = 2
        while i < n // 2:
             if n % 2 == 0:
                  return False
             return True

num = int(input("insert number: "))
num1 = num + 1 
while not is_simple(num1):
      num1 += 1 

print(f'larger number than num that is simple is equal to: {num1}')

