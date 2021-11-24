#  Universidad Nacional de Costa Rica
#  II Proyecto de Estructuras de Datos
#  Analizador Semántico
#  Profesor: José Calvo Suárez
#  Autores Dayana Gibellato y Gianluca Gibellato

class SymbolTable(object):
    def __init__(self):
        self._dict = {}

    # returns the ascii value of the first letter of the token name
    def _first_letter_name(self, token):
        return ord(token.get_name()[0])

    # returns the ascii value of the last letter of the token name
    def _last_letter_name(self, token):
        return ord(token.get_name()[-1])

    # takes first and last letter of the token's name and calculates the hash
    def _hashing_function(self, token):
        return (self._first_letter_name(token) + self._last_letter_name(token)) % 20

    def insert(self, token):
        key = self._hashing_function(token)
        if not self.look_up(key):
            self._dict[key] = [token]
        else:
            self._dict[key].append(token)

    def look_up(self, key):  # cheks if a token is in the table
        try:
            var = self._dict[key]
            if var:
                return True
        except KeyError:
            return False

    def get_token(self, token):  # return the token if exists, return None otherwise
        key = self._hashing_function(token)
        if self.look_up(key):
            for i in self._dict[key]:
                if i.get_name() == token.get_name() and i.get_scope() <= token.get_scope():
                    return i
        return None

    def set_value(self, key, token):
        if self._look_up(key):
            self._dict[key] = token

    def printTable(self):
        for key, value in self._dict.items():
            for v in value:
                print(key, ':', v.__str__())
        print("\n")

# https://www.tutorialspoint.com/compiler_design/compiler_design_symbol_table.htm
