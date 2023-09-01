Ci sono due attributi che categorizzano le sequenze. Tipo di contenuto e mutabilità:

----- Container vs Flat

- Container sequences
Contengono elementi di tipologia differente. Mantiene le referenze a tali elementi.
list, tuple, collections.deque

- Flat sequences
Contengono elementi di stessa tipologia. Contiene il valori degli elementi.
str, bytes, array.array

----- Mutable vs Immutable
Le sequenze mutabili ereditano tutti i metodi dalle sequenze immutabili ed implementano metodi ulteriori.

- Mutable sequences
list, bytearray, array.array, collections.deque

- Immutable
tuple, str, bytes