import Token


class SymbolTable(object):
    def __init__(self):
        self._dict = {}

        # store the names of all entities
        # verify if a variable has been declared
        # determine the scope of a name

    # returns the ascii value of the first letter of the token name
    def _first_letter_name(self, token):
        return ord(token.get_name()[0])

    # returns the ascii value of the last letter of the token name
    def _last_letter_name(self, token):
        return ord(token.get_name()[-1])

    # takes first letter of token name and calculates the hash
    def _hashing_function(self, token):
        return (self._first_letter_name(token) + self._last_letter_name(token)) % 20

    def insert(self, token):
        key = self._hashing_function(token)
        if not self.look_up(key):
            self._dict[key] = [token]
        else:
            self._dict[key].append(token)

    def look_up(self, key):
        try:
            var = self._dict[key]
            if var:
                return True
        except KeyError:
            return False

    def get_token(self, token):
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
            #print(key, ' : ', end='')
            for v in value:
                print(key, ':', v.__str__())
        print("\n")

# https://www.tutorialspoint.com/compiler_design/compiler_design_symbol_table.htm
