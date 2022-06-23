for i in range(1, 101):
        if i % 5 != 0 and i % 3 != 0:
                print(f'answer is: {i}')
        elif i % 5 != 0 and i % 3 == 0:
                print(f'answer is: Fizz')
        elif i % 5 == 0 and i % 3 != 0:
                print(f'answer is: Buzz')
        elif i % 5 == 0 and i % 3 == 0:
                print(f'answer is: Fizz-Buzz')
