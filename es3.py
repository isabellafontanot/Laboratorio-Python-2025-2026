import sys
import argparse

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
def esegui_punto_1():
    print("Visualizzazione rubrica")
    for nome in rubrica: 
        dati = rubrica[nome]
        output = f"'{nome}'"
        for chiave in dati: 
            valore = dati[chiave]
            if type(valore) == str:
                output = output + f", '{chiave}' '{valore}'"    
            else:
                output = output + f", '{chiave}' '{valore}'"
        print(output)

#punto 2
def esegui_punto_2():
    print("Lista età ordinata")
    lista_age = []
    for nome in rubrica: 
        age = rubrica[nome]['età']
        lista_age.append(age) 

    lista_age.sort()
    print("Listà età in ordine crescente:", lista_age)
    print("Nomi in ordine crescente di età:")

    for age_corrente in lista_age:
        for nome in rubrica:
            if rubrica[nome]['età'] == age_corrente:
                template = '{}, {} anni'
                out = template.format(nome, age_corrente)
                print(out)
        
#punto 3
def esegui_punto_3():
    print("Inversione Lista")
    lista_age.reverse()
    print("Lista età invertita:", lista_age)

#punto 4
def esegui_punto_4(nome_specifico=None):
    if nome_specifico:
        # Stampo solo per la persona indicata
        if nome_specifico in rubrica:
            dati = rubrica[nome_specifico]
            desinenza = 'o' if dati['sesso'] == 'M' else 'a'
            template = 'Car{} {}, sei nat{} il {} di {} del {} e quindi a breve compirai {} anni. Ti manderemo gli auguri a {}.'
            out = template.format(desinenza, nome_specifico, desinenza, dati['giorno'], dati['mese'], dati['anno'], dati['età'], dati['mail'])
            print(out)
        else:
            print(f"Errore: {nome_specifico} non è presente in rubrica.")
    else:
        # Stampiamo per tutti 
        print("Messaggi personalizzati")
        for nome in rubrica:
            dati = rubrica[nome]
            desinenza = 'o' if dati['sesso'] == 'M' else 'a'
            giorno = dati['giorno']
            mese = dati['mese']
            anno = dati['anno']
            età = dati['età']
            mail = dati['mail']
            template = 'Car{} {}, sei nat{} il {} di {} del {} e quindi a breve compirai {} anni. Ti manderemo gli auguri a {}.'
            out = template.format(desinenza, nome, desinenza, giorno, mese, anno, età, mail)
            print(out)

#oppure dire a .format() di prendere i valori direttamente dentro dati usando le parentesi quadre

#punto 5
if len(sys.argv) == 2 and sys.argv[1] in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
    chiave_richiesta = sys.argv[1]
    print(f"Valori per la chiave '{chiave_richiesta}' ")
    for nome in rubrica:
        print(f"{nome}: {rubrica[nome][chiave_richiesta]}")
    sys.exit()

#punto 6 e 7

parser = argparse.ArgumentParser(description="Gestione rubrica")
parser.add_argument('--nome', type=str, help="Esegue il punto 4 solo per il nome indicato")
parser.add_argument('--punto1', action='store_true', help="Esegue il punto 1")
parser.add_argument('--lista_ordinata', action='store_true', help="Esegue il punto 2")
parser.add_argument('--punto3', action='store_true', help="Esegue il punto 3")
parser.add_argument('--punto4', action='store_true', help="Esegue il punto 4 per tutti")


args = parser.parse_args()

# Esecuzione dei punti in base alle scelte dell'utente
if args.nome:
    print(f"Messaggio mirato per {args.nome}") # Aggiunta 'f' mancante
    esegui_punto_4(args.nome) # Chiamiamo la funzione passandole il nome!

if args.punto1:
    esegui_punto_1()
    
if args.lista_ordinata:
    esegui_punto_2()
    
if args.punto3:
    esegui_punto_3()
    
if args.punto4:
    esegui_punto_4()

#per controllare i punti 5,6,7:
#python esercizio_3.py mail
#python esercizio_3.py --nome "Madoka Ayukawa"
#python esercizio_3.py --lista_ordinata