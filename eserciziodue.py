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