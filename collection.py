list = [4, 5, 6, 7, 8, 9]
list.pop()

print(list)

tuple = (4, 5, 6, 7, 8, 9, 9)
numbers = tuple.count(9)
print(tuple, numbers)

dictionary = {'name': 'Adam',
              'profession': 'doctor',
              'age': 45,
              'gender': 'male'}
print(dictionary)

num = {1, 2, 3, 4, 5877, 543, 23, 231, 2, 1}
print(num)

froz = frozenset(num)
print(froz)
