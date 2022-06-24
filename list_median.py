def get_median(data):
      '''this function returns your list median that you give him as an argument.'''
      sum = 0
      count = 0
      for num in data:
           sum += num
           count += 1 
      return sum / count

data = [1, 34, 4, 8]
print(f'median of data is equal to: {get_median(data)}')
