data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letters = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)

    else:
        numbers.append(i)

numbers.remove(6.13)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(1, 2)
numbers.sort()


numbers[0] **= 2
numbers[1] **= 2
numbers[2] **= 2

letters[1] = 'c'
letters[-2] = 'G'
letters.reverse()

print(tuple(numbers), tuple(letters))

