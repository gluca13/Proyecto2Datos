#  Universidad Nacional de Costa Rica
#  II Proyecto de Estructuras de Datos
#  Analizador Semántico
#  Profesor: José Calvo Suárez
#  Autores Dayana Gibellato y Gianluca Gibellato

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
        # If it finds a { or ( it will put it in the queue, if it finds a } or ) it will get it out from the queue, the scope is the size of the queue
        self._actualScope = queue.Queue()
        self._code = self._reader.read_from_file()  # Stores the code read from the file
        self.charactersDic = {'(': ' ( ', ')': ' ) ', '{': ' { ', '}': ' } ', '"': ' " ', '“': ' “ ', '”': ' ” ', '.': ' . ', ',': ' , ', '=': ' = ', '<': ' < ', '>': ' > ', '+': ' + ', '-': ' - ',
                              '*': ' * ', '/': ' / ', '!': ' ! ', '&&': ' && ', '||': ' || ', '==': ' == ', '!=': ' != ', '<=': ' <= ', '>=': ' >= '}
        self._errorList = []

    def get_symbol_table(self):
        return self._symbol_table

    def get_plain_text(self):
        return self._reader.get_plain_text()

    # replaces all the characters in the line with the same character surrounded by spaces
    # this helps to isolate each word in the line [1]
    def replace_all(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    # the code will be stored in a list of lists, each list is a line, and each element in the list is a word
    def analize(self):
        functionToken = Token.Token()  # stores a function as a token
        returnToken = Token.Token()  # stores a return variable as a token
        for line in self._code:
            self._actualLine += 1
            line = self.replace_all(line, self.charactersDic)
            # splits the line into words, so each word and character is an element in the list
            words = line.split()
            typeFlag = False  # flag to check if the word is a data type
            stringFlag = False  # flag to check if the word is a string variable
            functionFlag = False  # flag to check if the word is a function
            returnFlag = False  # flag to check if the word is a return variable
            wordsCounter = 0
            equalFlag = False  # flag to check if the word is an equal sign
            errorFlag = False  # flag to check if there is an error in the line
            equalToken = Token.Token()  # stores the variable previous of an equal sign as a token

            for word in words:
                if errorFlag:
                    continue
                if word == '{' or word == '(':
                    self._actualScope.put(word)
                elif word == '}' or word == ')':
                    self._actualScope.get()
                if word in self._dataTypes:
                    type = word  # stores the data type
                    typeFlag = True
                elif typeFlag:
                    # if the word has a ( after it, it is a function
                    if len(words)-1 != wordsCounter and words[wordsCounter+1] == '(':
                        functionFlag = True
                    token = Token.Token(
                        type, word, self._actualScope.qsize(), self._actualLine, functionFlag)
                    self._symbol_table.insert(token)
                    if functionFlag:
                        functionToken = token
                    functionFlag = False
                    typeFlag = False
                # if the word is a ", the next word will be a string, or it will close the string
                elif word == '“' or word == '"' or word == '”':
                    stringFlag = not stringFlag
                else:
                    if word in self._reservedWords or word in self.charactersDic:
                        if word == 'return':
                            returnFlag = True
                        if word == '=':
                            equalFlag = True
                            equalToken = Token.Token(
                                '', words[wordsCounter-1], self._actualScope.qsize(), self._actualLine, False)
                            equalToken = self._symbol_table.get_token(
                                equalToken)  # gets the token of the variable previous of the equal sign and stores it in equalToken
                        wordsCounter += 1
                        continue

                    # if the variable previous of the equal sign is a string and the word is not a string, it will show an error of assignment
                    elif equalFlag and equalToken.get_type() == 'string' and not stringFlag:
                        self._errorList.append(
                            'Error - Line ' + str(self._actualLine) + ': \"' + equalToken.get_name() + '\" is type (' + equalToken.get_type() + '). Invalid assignment of its value')
                        errorFlag = True

                    elif word.isdigit():
                        if equalToken is not None:
                            # if an float variable is assigned to an int variable, it will show an error
                            if equalToken.get_type() == 'int' and len(words)-1 != wordsCounter and words[wordsCounter+1] == '.':
                                self._errorList.append(
                                    'Error - Line ' + str(self._actualLine) + ': \"' + equalToken.get_name() + '\" is type (' + equalToken.get_type() + '). Invalid assignment of its value')
                                errorFlag = True
                        wordsCounter += 1
                        continue

                    elif stringFlag:
                        # if the stringFlag is True, it means that the word is a string, so it will verify the equalToken's type to not be a string
                        if equalToken.get_type() == 'int' or equalToken.get_type() == 'float':
                            self._errorList.append(
                                'Error - Line ' + str(self._actualLine) + ': \"' + equalToken.get_name() + '\" is type (' + equalToken.get_type() + '). Invalid assignment of its value')
                            errorFlag = True
                        wordsCounter += 1
                        continue

                    else:
                        # creates a void token to store the word, then checks if the token is stored in the symbol table
                        token = Token.Token(
                            '', word, self._actualScope.qsize(), self._actualLine)
                        checkToken = self._symbol_table.get_token(token)
                        # if the token is not stored in the symbol table, it means it is not declared and will show an error
                        if checkToken is None:
                            self._errorList.append(
                                'Error - line ' + str(self._actualLine) + ': \"' + word + '\" is not declared in this scope')
                            errorFlag = True

                        else:
                            if equalFlag:
                                # checks if the equalToken's (variable before an = sign) type is the same as the variable following the equal sign
                                if equalToken.get_type() != checkToken.get_type():
                                    self._errorList.append(
                                        'Error - Line ' + str(self._actualLine) + ': \"' + equalToken.get_name() + '\" is type (' + equalToken.get_type() + '). Invalid assignment of its value.')
                                    errorFlag = True

                            if returnFlag:
                                returnToken = checkToken
                                # checks if the return variable type is the same as the function's return type
                                if returnToken.get_type() != functionToken.get_type() or functionToken.get_type() == 'void':
                                    self._errorList.append(
                                        'Error - line ' + str(self._actualLine) + ': the type of \"' + returnToken.get_name() + '\" (' + returnToken.get_type() + ') does not match with the function return type (' + functionToken.get_type() + ')')
                                    errorFlag = True
                                returnToken = Token.Token()
                                functionToken = Token.Token()
                                returnFlag = False
                wordsCounter += 1

    def print_errors(self):
        print("\u001b[31m", end="")
        for i in self._errorList:
            print(i)

# [1] https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
