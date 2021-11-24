#  Universidad Nacional de Costa Rica
#  II Proyecto de Estructuras de Datos
#  Analizador Semántico
#  Profesor: José Calvo Suárez
#  Autores Dayana Gibellato y Gianluca Gibellato

class Token(object):
    def __init__(self, type='', name='', scope=0, line=0, function=False):
        self._type = type
        self._name = name
        self._scope = scope
        self._line = line
        self._isFunction = function  # True if the token is a function, False otherwise

    def set_type(self, type):
        self._type = type

    def set_name(self, name):
        self._name = name

    def set_scope(self, scope):
        self._scope = scope

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_scope(self):
        return self._scope

    def __str__(self):
        return ('Type: ' + self._type + ', Name: ' + self._name + ', Scope: ' +
                str(self._scope) + ', Line: ' + str(self._line)) + ', Function: ' + str(self._isFunction)
