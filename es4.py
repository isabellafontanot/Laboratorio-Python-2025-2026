import json

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

#punto 1
file_rubrica = open('rubrica.txt', 'w')

for nome in rubrica:
    dati = rubrica[nome]
    riga = f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']}\n"
    file_rubrica.write(riga)

file_rubrica.close()

print("File 'rubrica.txt' generato correttamente!")

#per stamparlo devo guardare il punto 1 dell'es 3   

#punto 2
with open("rubrica.json", "w") as write_file:
    # scrive il contenuto serializzato del dizionario nel file object
    json.dump(rubrica, write_file, indent=4)

print("File 'rubrica.json' generato con successo!")

#punto 3
with open("rubrica.json", "r") as read_file:
    # carico i dati dal file e li rimetto dentro una variabile dizionario
    rubrica_caricata = json.load(read_file)

print("Visualizzazione dati letti da rubrica.json")
# stampo a schermo riga per riga per far vedere che li abbiamo letti
for nome in rubrica_caricata:
    dati = rubrica_caricata[nome]
    output = f"'{nome}'"
    for chiave in dati:
        output += f", '{chiave}': {dati[chiave]}"
    print(output)