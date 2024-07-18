number1 = 35
number2 = 3

try:
    resaul = number1 / number2
    print(resaul)
except ZeroDivisionError:
    print("Error, division by zero")
