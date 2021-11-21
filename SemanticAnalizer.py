import Reader
import SymbolTable
import queue
import Token


class SemanticAnalizer(object):
    def __init__(self, fileName):
        self._reader = Reader.Reader(fileName)
        self._symbol_table = SymbolTable.SymbolTable()
        self._dataTypes = ('void', 'int', 'float', 'string')
        self._reservedWords = ('if', 'while', 'return')
        self._actualLine = 0
        self._actualScope = queue.Queue()
        self._code = self._reader.read_from_file()
        self.charactersDic = {'(': ' ( ', ')': ' ) ', '{': ' { ', '}': ' } ', '"': ' " ', '“': ' “ ', '”': ' ” ', '.': ' . ', ',': ' , ', '=': ' = ', '<': ' < ', '>': ' > ', '+': ' + ', '-': ' - ',
                              '*': ' * ', '/': ' / ', '!': ' ! ', '&&': ' && ', '||': ' || ', '==': ' == ', '!=': ' != ', '<=': ' <= ', '>=': ' >= '}
        self._errorList = []

    def get_symbol_table(self):
        return self._symbol_table

    # replaces all the characters in the line with the same character surrounded by spaces
    # this helps to isolate each word in the line [1]
    def replace_all(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    def analize(self):
        functionToken = Token.Token()
        returnToken = Token.Token()
        for line in self._code:
            self._actualLine += 1
            line = self.replace_all(line, self.charactersDic)
            words = line.split()
            typeFlag = False
            stringFlag = False
            functionFlag = False
            returnFlag = False
            wordsCounter = 0
            for word in words:
                if word == '{' or word == '(':
                    self._actualScope.put(word)
                elif word == '}' or word == ')':
                    self._actualScope.get()
                if word in self._dataTypes:
                    type = word
                    typeFlag = True
                elif typeFlag:
                    if words[wordsCounter+1] == '(':
                        functionFlag = True
                    token = Token.Token(
                        type, word, self._actualScope.qsize(), self._actualLine, functionFlag)
                    self._symbol_table.insert(token)
                    if functionFlag:
                        functionToken = token
                    functionFlag = False
                    typeFlag = False
                elif word == '“' or word == '"' or word == '”':
                    stringFlag = not stringFlag
                else:  # if there is no type, before the idientifier
                    if word in self._reservedWords or word in self.charactersDic:
                        if word == 'return':
                            returnFlag = True
                        continue
                    elif word.isdigit():
                        continue
                    elif stringFlag:
                        continue
                    else:
                        token = Token.Token(
                            '', word, self._actualScope.qsize(), self._actualLine)
                    checkToken = self._symbol_table.get_token(token)
                    if checkToken is None:
                        self._errorList.append(
                            'Error - line ' + str(self._actualLine) + ': ' + word + ' is not declared in this scope')
                    else:
                        if returnFlag:
                            returnToken = checkToken
                            if returnToken.get_type() != functionToken.get_type():
                                self._errorList.append(
                                    'Error - line ' + str(self._actualLine) + ': the return value of \"' + returnToken.get_name() + '\" (' + returnToken.get_type() + ') does not match with the function type (' + functionToken.get_type() + ')')
                            returnToken = Token.Token()
                            functionToken = Token.Token()
                wordsCounter += 1

    def print_errors(self):
        for i in self._errorList:
            print(i)


# [1] https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
