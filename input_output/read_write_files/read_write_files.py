f = open("workfile") #<_io.TextIOWrapper name='workfile' mode='r' encoding='UTF-8'>

print(f.read())
f.close()

# buona norma utilizzare with per gestire correttamente la chiusura del file anche a fronte di eccezioni
with open("workfile") as f:
    read_data = f.read()
    print(read_data)

print(f.closed) # True

with open("workfile") as f:
    read_data = f.read(2)
    print(read_data) # Ci
    read_data = f.read()
    print(read_data) # ao mare
    f.seek(0,0) # offset, punto di partenza
    read_data = f.read()
    print(read_data) # Ciao mare

print("\n=== multi line file")
with open("multiline") as f:
    line = f.readline()
    print(line, end="")
    line = f.readline()
    print(line, end="")
    line = f.readline()
    print(line, end="")

print("\n=== multi line file foreach")
with open("multiline") as f:
    for line in f:
        print(line, end='')

print("\n=== multi line file readlines()")
with open("multiline") as f:
    print(f.readlines())