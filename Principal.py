import SymbolTable


def readFromFile(fileName):
    file = open(fileName, "r")
    text = file.read()
    file.close()
    return text


def writeToFile(fileName, text):
    file = open(fileName, "w")
    file.write(text)
    file.close()
