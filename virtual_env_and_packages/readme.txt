# Ogni volta che lavori su un progetto Python che utilizza dipendenze esterne installate con pip, è buona norma crare prima un ambiente virtuale.
python3 -m venv venv

# Attivare l'ambiente
source venv/bin/activate

# Installare in pacchetto
python -m pip install <package-name>

# Poiché abbiamo creato ed attivato un ambiente virutale, pip installerà il packages in un ambiente isolato.