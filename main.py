#read from file
path = '/Users/macbook/PycharmProjects/pythonProject/.venv/file.txt'
myFile = open(path, 'r')
myLines = myFile.read()
print(myLines)

#write and read
myFile =open(path, 'w+')
text = "\nМетушалах"
myFile.write(text)
myLines = myFile.read()
print(myLines)
myFile.close()