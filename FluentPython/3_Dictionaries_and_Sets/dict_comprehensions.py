# A dictcomp builds a dict instance by taking key:value pairs from any iterable
dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (86, 'China'), # ignored during dictcomp
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)

# se ho un iterable con elementi composti da 2 valori, posso passarlo direttamente al costruttore.
# il primo valore verrà utilizzato come chiave di default
trial = dict(dial_codes)
print(trial)
