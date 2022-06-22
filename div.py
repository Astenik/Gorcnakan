def divisiors(num:int):
        """This function returns list consists of number's divisiors."""
        i = 1
        div = []
        while i <= num:
            if num % i == 0:
                div.append(i)
            i += 1
        return div
            
n = int(input("insert number"))
print(f'divisors of your number are: {divisiors(n)}')


def divisior(n):
      """This function returns list consists of number's divisiors."""
      return [i for i in range(1, n) if n % i == 0] == n

m = int(input("insert number"))
print(divisior(m))
