from os import read
import SymbolTable
import Token


class Reader(object):

    def __init__(self, fileName):
        self._fileName = fileName

    def read_from_file(self):
        file = open(self._fileName, "r", encoding="utf8")
        textList = file.readlines()
        file.close()
        return textList
