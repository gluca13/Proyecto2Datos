from os import read
import SymbolTable
import Token


class Reader(object):

    def __init__(self, fileName):
        self._fileName = fileName

    def get_plain_text(self):
        try:
            file = open(self._fileName, "r", encoding="utf8")
            text = file.read()
            file.close()
        except FileNotFoundError:
            text = "File not found"
        except UnicodeDecodeError:
            text = "Unicode error"
        return text

    def read_from_file(self):
        try:
            file = open(self._fileName, "r", encoding="utf8")
            textList = file.readlines()
            file.close()
        except FileNotFoundError:
            textList = ["File not found"]
        return textList
