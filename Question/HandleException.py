try:
    div = 20 / 0
except ZeroDivisionError:
    print("Division by zero")
try:
    div2 = 30 / 0
except Exception as e:
    print("Opps, something wrong: {}".format(e))