s = 'café'
len(s) # 4

b = s.encode('utf8') # Codifica la stringa in bytes utilizzando UTF-8
print(b) # b'caf\xc3\xa9' --> b sta per bytes

# bytes b ha 5 bytes poiché il code point del carattere 'é' necessità di 2 byte in UTF-8
print(len(b)) # 5 
print(b.decode('utf8')) # café

# bytes can be built from a string given an encoding. Ogni elemento è un intero in un range [0 - 255]
cafe = bytes('café', encoding='utf_8')
print(cafe) # b'caf\xc3\xa9'
print(cafe[0]) # 99
print(cafe[-1:]) # b'\xa9'

cafe_arr = bytearray(cafe)
print(cafe_arr) # bytearray(b'caf\xc3\xa9') -> bytearray è mutabile
