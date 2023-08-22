try:
    x = int(input("Enter a number:\n"))
except ValueError:
    print("Ops! Inserire un numero valido")
except:
    print("Errore non gestito")
else:
    print(f"Numero inserito: {x}")
finally:
    print("Goodbye")

# raise an exception with argument
try:
    raise Exception("Andrea", "Bondanini")
except Exception as e:
    print(e.args) # ('Andrea','Bondanini')
    print(e.args[0]) # Andrea
