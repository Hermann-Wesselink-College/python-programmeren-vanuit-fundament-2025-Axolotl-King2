# Opdracht 1 tot en met 7 van pragraaf 2.10
from datetime import datetime
datumtijd = datetime.now()
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
uur = datumtijd.hour
minuut = datumtijd.minute
geboortejaar = int(input('In welk jaar ben je geboren?'))
geboortemaand = int(input('In welke maand ben je geboren?'))
geboortedag  = int(input('op welke dag ben je geboren?'))
datum1 = datetime(geboortejaar, geboortemaand, geboortedag)
datum2 = datetime.now()
verschil = datum2 - datum1
if maand <= 3 and dag <= 28:
    uur += 1
if maand >= 10 and dag >= 26:
    uur += 1
print('De datum van vandaag is '+str(dag)+'-'+str(maand)+'-'+str(jaar)+' en het is nu '+ str(uur)+':'+str(minuut))
print('Je bent '+ str(verschil.days)+' dagen oud. En '+ str(verschil.year)+' jaar oud.')