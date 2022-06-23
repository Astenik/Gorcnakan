def average(lst):
       """this function counts your list average."""
       return sum(lst) / len(lst)
    

data = [90, 6, 5, 8]
nums = []
nums.append(int(input("insert the list: ")))
i = 0
while nums[i] != 0:
      nums.append(int(input("insert the list: ")))
      i += 1

print(f'the average of your lis is: {average(data)}')
print(f'the smaller numbers from average are: {[i for i in range(len(data)) if i < average(data)]}')
print(f'the equal numbers to average are: {[i for i in range(len(data)) if i == average(data)]}')
print(f'the larger numbers from average are: {[i for i in range(len(data)) if i > average(data)]}')



