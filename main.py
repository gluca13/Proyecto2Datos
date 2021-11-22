import SymbolTable
import Token
import Reader
import SemanticAnalizer


s = SemanticAnalizer.SemanticAnalizer('file2.txt')

s.analize()

st = s.get_symbol_table()

st.printTable()

print(s.get_plain_text())

s.print_errors()
