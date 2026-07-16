#punto 1

import itertools
import time

def stessa_diagonale(x0, y0, x1, y1):
    """Ritorna Vero se le posizioni (x0, y0) e (x1, y1) sono sulla stessa diagonale"""
    dy = abs(y1 - y0)  # distanza lungo y
    dx = abs(x1 - x0)  # distanza lungo x
    return dx == dy

def incrocia_colonne(posizioni, col):
    """Ritorna Vero se la regina nella colonna 'col' (ultima colonna) incrocia la diagonale
    di una delle regine nelle colonne precedenti."""
    # Controllo tutte le precedenti fino a questa 'col'
    for c in range(col):
        # x è la colonna (c), y è la riga (posizioni[c])
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True  # Si scontrano!
    return False

soluzioni_valide = []
tentativi = 0
tempo_inizio = time.time()

# Genero le mosse, ognuna è una lista di 8 numeri
for mossa in itertools.permutations(range(8)):
    tentativi = tentativi + 1
    
    # Verifico se questa mossa è valida
    valida = True
    # Controlliamo tutte le colonne dalla seconda (1) fino all'ottava (7)
    for colonna in range(1, 8):
        if incrocia_colonne(mossa, colonna):
            valida = False # Se incrocia, questa mossa non è buona
            break          # Inutile controllare le altre colonne, saltiamo oltre
            
    # Se la mossa ha superato tutti i controlli ed è valida...
    if valida == True:
        soluzioni_valide.append(mossa) # La salvo
        
        # Se abbiamo raggiunto le 10 soluzioni richieste, ci fermiamo
        if len(soluzioni_valide) == 10:
            break

tempo_fine = time.time()

tempo_totale = tempo_fine - tempo_inizio
tempo_medio = tempo_totale / 10

print("Ho trovato le 10 soluzioni")
print("Tentativi totali fatti dal programma:", tentativi)
print("Tempo medio per trovare una soluzione:", tempo_medio, "secondi")

#punto 2
soluzioni_valide = []
tentativi_per_soluzione = []  # Lista dove salveremo i tentativi di ciascuna soluzione
tentativi_correnti = 0        # Questo contatore ricomincia da zero ogni volta che troviamo una soluzione

for mossa in itertools.permutations(range(8)):
    tentativi_correnti = tentativi_correnti + 1  # Aumentiamo i tentativi ad ogni giro
    
    valida = True
    for colonna in range(1, 8):
        if incrocia_colonne(mossa, colonna):
            valida = False
            break
            
    if valida == True:
        soluzioni_valide.append(mossa)
        # Salviamo i tentativi fatti per QUESTA soluzione
        tentativi_per_soluzione.append(tentativi_correnti) 
        # IMPORTANTE: Azzeriamo il contatore per la prossima soluzione!
        tentativi_correnti = 0 
        
        if len(soluzioni_valide) == 10:
            break

# Stampiamo i risultati
for i in range(10):
    print(f"La soluzione {i+1} ha richiesto {tentativi_per_soluzione[i]} tentativi.")

#punti 3 e 4
soluzioni_uniche = []
conteggio_ripetizioni = {} # Dizionario vuoto per contare le frequenze

for mossa in soluzioni_valide:
    # Trasformiamo la mossa in una tupla, perché le liste non possono essere usate come chiavi nei dizionari
    mossa_tupla = tuple(mossa)
    
    # Se la mossa NON è ancora nel dizionario, significa che è la prima volta che la vediamo
    if mossa_tupla not in conteggio_ripetizioni:
        conteggio_ripetizioni[mossa_tupla] = 1
        soluzioni_uniche.append(mossa_tupla) # La salviamo tra le uniche
    else:
        # Se c'è già, aumentiamo il suo contatore di 1
        conteggio_ripetizioni[mossa_tupla] = conteggio_ripetizioni[mossa_tupla] + 1

print(f"Abbiamo trovato {len(soluzioni_uniche)} soluzioni uniche.")
for sol, volte in conteggio_ripetizioni.items():
    print(f"La soluzione {sol} compare {volte} volta/e.")

#punto 5
def risolvi_nxn(N):
    '''Generalizzo il problema per una scacchiera NxN'''
    soluzioni = []

    for mossa in itertools.permutations(range(N)):
        valida = True

        for colonna in range(1, N):
            if incrocia_colonne(mossa, colonna):
                valida = False
                break
        if valida == True: 
            soluzioni.append(mossa)

    return soluzioni

# Esempio
risultati_5x5 = risolvi_nxn(5)
print(f"Una scacchiera 5x5 ha in totale {len(risultati_5x5)} soluzioni.")

#punto 6
N = 4 #in questa esistono esattamente 2 soluzioni valide, scacchiera 2x2 e 3x3 troppo piccole
tempo_scaduto = False

while not tempo_scaduto:
    print(f"Tentiamo con una scacchiera {N}x{N}...")
    
    tempo_inizio = time.time()
    
    # Cerchiamo SOLO LA PRIMA soluzione 
    soluzione_trovata = False
    for mossa in itertools.permutations(range(N)):
        valida = True
        for colonna in range(1, N):
            if incrocia_colonne(mossa, colonna):
                valida = False
                break
        if valida == True:
            soluzione_trovata = True
            break # Abbiamo trovato la prima soluzione, usciamo dal ciclo for
            
    tempo_fine = time.time()
    tempo_impiegato = tempo_fine - tempo_inizio
    
    print(f"-> Tempo impiegato: {tempo_impiegato:.4f} secondi.")
    
    # Se il tempo supera i 15 secondi, ci fermiamo
    if tempo_impiegato > 15.0:
        print(f"\nLa scacchiera più grande risolvibile in meno di 15s è: {N - 1}x{N - 1}")
        tempo_scaduto = True
    else:
        N = N + 1 # Proviamo la scacchiera successiva

#punto 7
# Funzione per ruotare di 90 gradi una volta
def ruota_90(scacchiera):
    N = len(scacchiera)
    # Creiamo una lista vuota di N elementi
    nuova_scacchiera = [0] * N
    for colonna in range(N):
        riga = scacchiera[colonna]
        # Applichiamo la regola geometrica di rotazione
        nuova_scacchiera[riga] = (N - 1) - colonna
    return tuple(nuova_scacchiera)

# Ora troviamo 5 soluzioni che siano geometricamente del tutto diverse tra loro
soluzioni_uniche_strutturali = []
tutte_le_simmetrie_viste = set() # Usiamo un set per ricordarci cosa abbiamo già visto

for mossa in itertools.permutations(range(8)):
    if scacchiera_valida(mossa):
        mossa_tupla = tuple(mossa)
        
        # Se questa soluzione non è né se stessa né una rotazione di una già trovata...
        if mossa_tupla not in tutte_le_simmetrie_viste:
            soluzioni_uniche_strutturali.append(mossa_tupla)
            
            # Calcoliamo le sue 4 versioni (0°, 90°, 180°, 270°)
            r0 = mossa_tupla
            r90 = ruota_90(r0)
            r180 = ruota_90(r90)
            r270 = ruota_90(r180)
            
            # Le aggiungiamo tutte all'elenco delle cose già viste, così non le consideriamo in futuro
            tutte_le_simmetrie_viste.update([r0, r90, r180, r270])
            
            # Ci fermiamo quando abbiamo i 5 gruppi richiesti
            if len(soluzioni_uniche_strutturali) == 5:
                break

# Stampiamo i 5 gruppi di simmetrie
for i, sol in enumerate(soluzioni_uniche_structural, 1):
    r0 = sol
    r90 = ruota_90(r0)
    r180 = ruota_90(r90)
    r270 = ruota_90(r180)
    print(f"\n--- GRUPPO SOLUZIONE UNICA {i} ---")
    print("Originale (0°): ", r0)
    print("Ruotata 90°:    ", r90)
    print("Ruotata 180°:   ", r180)
    print("Ruotata 270°:   ", r270)