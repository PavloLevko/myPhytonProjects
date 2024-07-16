import re

#open and read file
pach = "/Users/macbook/PycharmProjects/pythonProject/.venv/file.txt"
file = open(pach, "r")
text = file.read()

#simple condition
if re.search(r"\d", text):
    print("Text hes digits", re.findall(r"\d+", text))
else:
    print("Digits is absent")
