#  Universidad Nacional de Costa Rica
#  II Proyecto de Estructuras de Datos
#  Analizador Semántico
#  Profesor: José Calvo Suárez
#  Autores Dayana Gibellato y Gianluca Gibellato

import SemanticAnalizer


s = SemanticAnalizer.SemanticAnalizer(
    'file3.txt')  # receives the file to be analized

s.analize()

st = s.get_symbol_table()

st.printTable()

print(s.get_plain_text())

s.print_errors()
