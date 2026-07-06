#punto 1
def is_pari(n): 
    '''controllo se il numero è pari'''

    if n%2 == 0:
        return True
    else:
        return False
        
res = is_pari(4)
print(res)
res = is_pari(5)
print(res)

#punto 2 
def prendere_input_valido():
    '''continuare a richiedere valore finchè input è corretto'''
    while True: 
      try: 
         numero = int(input("Inserisci un numero intero positivo (> 0)"))
         if numero > 0:
             return numero
         else: 
             print("Il numero deve essere > 0. Riprova")
      except ValueError: 
        print("Input non valido. Devi inserire un numero > 0")

numero_scelto = prendere_input_valido()

print("La funzione ha restituito con successo il numero:", numero_scelto)

#punto 3
def generare_lista(n):
    '''generare una lista seguendo delle regole in base se il numero è pari o dispari'''
    lista = [n]
    while n!= 1 and len(lista) <= 100:
        if is_pari(n):
            n = n/2
        else: 
            n = n * 3 + 1
        lista.append(n)
    return lista 

lista_risultato = generare_lista(numero_scelto)
print("La lista generata è: lista_risultato")

#punto 4 
def analizza_sequenza(lista): 
    '''genera tre valori dalla lista ricevuta'''
    massimo = max(lista)
    lunghezza = len(lista)
    somma = sum(lista)
    return massimo, lunghezza, somma

#punto 5
def ricerca(lista):
    '''stampare numeri divisibili per 5, altrimenti risultato dedicato'''
    trovato = False
    print("Numeri della lista divisibili per 5:")
    for numero in lista: 
        if numero % 5 == 0: 
            print(numero)
            trovato = True
    if not trovato:
        print("Nessun numero nella lista è divisibile per 5.")

#punto 6
def main():
    '''funzione principale'''
    print("=== PROGRAMMA DI ANALISI SEQUENZE ===")
    
    while True:
        try:
            quanti = int(input("Quanti numeri vuoi testare in totale? "))
            if quanti > 0:
                break
            print("Inserisci un numero maggiore di zero.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")
            
    max_lunghezza_registrata = -1
    numero_piu_lungo = None
    
    for i in range(quanti):
        print(f"\n Test {i + 1} di {quanti}")
        
        num_iniziale = prendere_input_valido()
        
        lista_generata = generare_lista(num_iniziale)
        print(f"Sequenza generata: {lista_generata}")
        
        massimo, lunghezza, somma = analizza_sequenza(lista_generata)
        print(f"Analisi: Valore Massimo = {massimo} | Lunghezza = {lunghezza} | Somma = {somma}")
        
        ricerca(lista_generata)
        
        if lunghezza > max_lunghezza_registrata:
            max_lunghezza_registrata = lunghezza
            numero_piu_lungo = num_iniziale

    print("\n================ RIEPILOGO ================")
    print(f"Il numero iniziale che ha generato la sequenza più lunga è stato: {numero_piu_lungo}")
    print(f"La lunghezza di questa sequenza è di {max_lunghezza_registrata} elementi.")
    print("===========================================")

if __name__ == "__main__":
    main()

