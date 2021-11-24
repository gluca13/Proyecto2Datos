#  Universidad Nacional de Costa Rica
#  II Proyecto de Estructuras de Datos
#  Analizador Semántico
#  Profesor: José Calvo Suárez
#  Autores Dayana Gibellato y Gianluca Gibellato

import os


class Reader(object):

    def __init__(self, fileName):
        self._fileName = fileName

    def get_plain_text(self):
        try:
            file = open(self._fileName, "r", encoding="utf8")
            text = f"\033[94m----------------------------------------- \nFile {self._fileName} \033[0m \n\n"
            text += file.read()
            text += "\033[94m \n----------------------------------------- \033[0m \n"
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
            print("\u001b[31m")
            print(f"File \"{self._fileName}\" not found")
            os._exit(1)
        return textList
