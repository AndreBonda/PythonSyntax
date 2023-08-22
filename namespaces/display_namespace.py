from module.fibonacci import fibonacci

'''Demo docstring'''

foo = "Andrea"

def fooFunc():
    pass

# stampa i valori del namespace. Include i nomi di variabili e funzioni locali. Include fibonacci poiché è un è una funzione importata
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fibonacci', 'foo', 'fooFunc']
print(__doc__) # Demo docstring
print(__file__) # /Users/andrea/Personal/LearningPython/namespaces/display_namespace.py