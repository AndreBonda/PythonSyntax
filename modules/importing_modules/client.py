# in questo modo importo il modulo con la propria symbol table
import fibonacci

# in questo modo importo il nome (fibonacci_recursive) direttamente nella symbol table
# di questo modulo chiamante.
# È possibile anche importare tutti i nomi dal modulo from module import *
from fibonacci_recursive import fibonacci_recursive

fibonacci.fibonacci(11)
fibonacci_recursive(11)

print(dir(__builtins__))