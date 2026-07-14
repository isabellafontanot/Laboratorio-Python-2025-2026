#punto 1 
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

righe = testo.splitlines()
contatore_righe = 0 

for riga in righe:
    if riga.strip() != "":
        contatore_righe += 1

print("Righe non vuote:", contatore_righe)

#punto 2 
parole = testo.split()
numero_parole = len(parole)
print("Numero totale di parole:", numero_parole)

#punto 3 
contatore_alfanumerici = 0

for carattere in testo: 
    if carattere.isalnum() :
        contatore_alfanumerici += 1

print("Caratteri alfanumerici:", contatore_alfanumerici)

#punto 4
lettera_utente = input("Inserire una lettera da cercare")

testo_minuscolo = testo.lower()
lettera_minuscola = lettera_utente.lower()

conteggio_lettera = testo_minuscolo.count(lettera_minuscola)

template = "La lettera {} compare {} volte."
out = template.format(lettera_utente, conteggio_lettera)
print(out)

#punto 5
testo_modificato = testo.replace("day", "PYTHON").replace("Day", "PYTHON")
testo_modificato = testo_modificato.replace("water", "PYTHON").replace("Water", "PYTHON")
testo_modificato = testo_modificato.replace("about", "PYTHON").replace("About", "PYTHON")

print("Testo con sostituzioni:\n", testo_modificato)

#punto 6 
parole = testo.split()
parole_nuove = []

for indice, parola in enumerate(parole):
    if (indice + 1) % 2 != 0: 
        parole_nuove.append(parola.upper())
    else: 
        parole_nuove.append(parola) 

testo_dispari_maiuscolo = " ".join(parole_nuove)
print("Testo con parole dispari in maiuscolo:\n", testo_dispari_maiuscolo)

#punto 7 
righe = testo.splitlines()
righe_invertite = righe[::-1]

testo_righe_invertite = "\n".join(righe_invertite)
print("Testo con righe invertite:\n", testo_righe_invertite)

#punto 8 
strofe_modificate = []
for strofa in testo: 
    nuova_strofa = list(strofa) 
    if len(nuova_strofa) > 1: 
        nuova_strofa[1] = nuova_strofa[1][::-1]
    strofe_modificate.append("\n".join(nuova_strofa))

testo_specchio = "\n\n".join(strofe_modificate)
print(testo_specchio)

#punto 9 
def estrai_parole(testo_da_pulire):
   '''Tolgo punteggiatura e maiuscole'''
   pulito = re.sub(r"[^a-zA-Z0-9\s]", " ", testo_da_pulire.lower())
   return pulito.split()

parole_per_strofa = [set(estrai_parole(" ".join(s))) for s in strofa]
parole_comuni = set.intersection(*parole_per_strofa)

print("Parole comuni a tutte le strofe:", list(parole_comuni))

#punto 10 
testo_minuscolo = testo.lower()
testo_senza_punteggiatura = re.sub(r"[^a-zA-Z0-9\s]", " ", testo_minuscolo)
tutte_le_parole = testo_senza_punteggiatura.split()

print("Numero di parole totali (con duplicati):", len(tutte_le_parole))

insieme_parole_uniche = set(tutte_le_parole)
lista_parole_uniche = list(insieme_parole_uniche)

print("Numero di parole uniche (senza duplicati):", len(lista_parole_uniche))

lista_ordinata = sorted(lista_parole_uniche, key=lambda word: (len(word), word))

print("Lista finale")
print(lista_ordinata)

#punto 11
freq_caratteri = {}

for carattere in testo:
    freq_caratteri[carattere] = freq_caratteri.get(carattere, 0) + 1

print("Conteggio di tutti i caratteri")

for chiave in sorted(freq_caratteri.keys()):
    template = "Carattere {} trovato {} volte." 
    out = template.format(repr(chiave), freq_caratteri[chiave])
    print(out)

#punto 12 

freq_alfanumerici = {}

testo_minuscolo = testo.lower()

for carattere in testo_minuscolo:
    if carattere.isalnum():
        freq_alfanumerici[carattere] = freq_alfanumerici.get(carattere, 0) + 1

print("Solo caratteri alfanumerici")

for chiave in sorted(freq_alfnumerici.keys()):
    template = "Lettera {} trovata {} volte." 
    out = template.format(chiave, freq_alfanumerici[chiave])
    print(out)
