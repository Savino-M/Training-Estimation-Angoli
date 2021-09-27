Training Estimation è un'applicazione pensata per aiutare gli utenti meno esperti nello svolgimento di esercizi fisici. L'utente accede all'app tramite face recognition e può caricare la propria scheda di allenamento. Al momento gli esercizi supportati sono i bicipiti e gli squat. Per aggiungerne altri, bisogna
solamente inserire le relative risorse.


La struttura della repository si presenta nel seguente modo:

|–– doc
|    |–– video
|-- res
|    |-- esercizi
|    |-- icone
|    |-- schede esercizi
|    |-- sounds
|    |-- utenti
|    |-- video
|–– src


Nel seguito si dettagliano i ruoli dei diversi componenti:

- doc: in questa cartella si trova tutta la documentazione relativa al progetto;

- res: contiene le risorse utilizzate dall'applicazione:
	- esercizi contiene il dataframe di 'esempio' dell'esercizio e il classificatore, per esercizio
	- icone contiene le icone dell'app
	- schede esercizi contiene le schede di allenamento dei vari utenti
	- sounds contiene i file audio che vengono utilizzati per l'interazione
    - utenti contiene le foto dei volti degli utenti registrati
    - video contiene i video di esempio degli esercizi

- src: la cartella principale del progetto, in cui si trova il codice dell’applicazione

Questa variante dell'applicazione determina l'esecuzione corretta dell'esercizio calcolando gli angoli
