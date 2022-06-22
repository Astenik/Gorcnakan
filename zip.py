def zip(data1, data2):
        """this function combinates two lists and constracts new list where
               list[i] = [data1[i], data2[i]]
               data1 is your firs argument and data2 is your second argument."""
                
        lst = [None] * len(data1)
        for i in range(len(data1)):
             lst[i] = [data1[i], data2[i]]
        
        return lst

data1 = [0, 6, 8]
data2 = [9, 56, 7]
print(zip(data1, data2))
  
