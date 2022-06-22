def is_polindrom(n):
        """this function checs is your sentence polindrom or not."""
        list = [None] * len(n)
        i = 0
        j = len(n) - 1 
        while i < len(n):
             list[i] = n[j]
             i += 1 
             j -= 1 
        return list == n 
        
sentenses = input("insert the sentence: ")
print(f'is tour sentence polindrom? {is_polindrom(sentenses)}')
    
