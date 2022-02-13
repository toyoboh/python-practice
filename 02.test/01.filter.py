def isEven(number):
    if number % 2 == 0:
        print(f'This number, {number} is even!')
        # return True
    else:
        print(f'This number, {number} is odd!')
        # return False

numbers = [0, 8, -4, 9, -3, 2]

# print(list(filter(isEven, numbers)))

new_list = list(filter(isEven, numbers))
print(new_list)
