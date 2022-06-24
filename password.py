import random
def random_passwd(n):
        '''this function creates password for you with n symbols from ASCII symbols: from 33 to 126 where n function's argument.'''
        passwd = ' '
        i = 0 
        while i < n:
              passwd =  passwd + chr(random.randint(33, 126))
              i += 1 
        return passwd

print(random_passwd(8))
