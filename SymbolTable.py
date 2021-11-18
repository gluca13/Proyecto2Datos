class SymbolTable:
    def __init__(self):
        self._dict = {}
        self._dataTypes = ['void','int','float','string']
        self._reservedWords = ['if', 'while', 'return']
        #self._signs = ['(', ')', '{', '}', ',', '=', '<', '>', '+', '-', '/', '*']

        dist = 'v' - 'a' % 20
        # store the names of all entities
        # verify if a variable has been declared
        # determine the scope of a name

    def insert(self):
        pass

    def lookup(self):
        pass

    # def isInTable(self, key):
    #     for key in self._dict:
    #         if key == key:
    #             return True
    #     return False

    # def getValue(self, key):
    #     if self.isInTable(key):
    #         return self._dict[key]
    #     return None

    # def setValue(self, key, value):
    #     self._dict[key] = value

    # def insertValue(self, key, value):
    #     self._dict[key] = value

    # def deleteValue(self, key):
    #     if self.isInTable(key):
    #         del self._dict[key]
    #         return True
    #     return False

    # def printTable(self):
    #     for key in self._dict:
    #         print(key, self._dict[key])

# https://www.tutorialspoint.com/compiler_design/compiler_design_symbol_table.htm