# importo un modulo individuale dal package.
# devo referenziarlo con il nome completo
import sound.effects.echo
sound.effects.echo.echo_a()

# alternativa per importare un modulo individuale evitando l'utilizzo del prefisso
from sound.effects import echo
echo.echo_b()

# importo direttamente la funzione
from sound.effects.echo_v2 import echo_v2_b
echo_v2_b()

from sound.filters import filters
filters.filter_a()