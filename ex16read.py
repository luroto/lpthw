from sys import argv

script, filename = argv

filecillo = open(filename, 'r')
print(filecillo.read())
print("We're going to close it")
filecillo.close()
