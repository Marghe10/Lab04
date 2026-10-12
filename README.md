# Lab 04

#### Argomenti

- Lettura su file (continuazione).
- Eccezioni (continuazione).
- Classi e oggetti (metodi dunder, getter e setter, collezioni di e relazioni tra oggetti).
- Ordinamento (di oggetti).
- Ereditarietà
- Polimorfismo

---

## Lingotto Fiere

Il laboratorio prevede la progettazione di un sistema per la gestione degli stand all'interno del centro
fieristico Lingotto Fiere, utilizzato per organizzare le fiere ed esposizioni ospitate al suo interno. Il
centro è identificato semplicemente da un nome e rappresenta l'elemento centrale attorno al quale ruota
l'intero sistema. Al suo interno si trovano due insiemi principali: quello degli stand, che possono avere
caratteristiche diverse tra loro, e quello degli espositori, che rappresentano le aziende registrate che
possono richiedere uno stand.
Tutte le informazioni necessarie per gestire il sistema sono raccolte in un unico file, denominato
`dati_lingotto.csv`. Questo file contiene sia i dati relativi agli stand, sia quelli riguardanti gli
espositori. Ogni riga del file corrisponde a un elemento ben preciso: uno stand oppure un espositore.

Le righe dedicate agli stand contengono sempre un codice univoco (ad esempio `ST1`, `ST2`, ..., `STN`),
seguito dalla superficie in metri quadri dello stand, dal padiglione in cui esso si trova e dal prezzo di
base per l'intera fiera. Alcuni stand, oltre alle informazioni di base, possono presentare delle
caratteristiche aggiuntive che ne definiscono la tipologia. Se dopo il prezzo è presente un valore numerico,
la riga fa riferimento a uno stand dotato di prese elettriche aggiuntive: il numero indicato rappresenta la
quantità di prese extra disponibili. Se invece il valore aggiuntivo è una stringa di testo, lo stand è di
tipo Premium e la stringa specifica la posizione, ad esempio `Ingresso`, `Angolare` o `Vetrina`.

Le righe relative agli espositori, invece, hanno una struttura più semplice: riportano un codice univoco che
identifica l'espositore (ad esempio `ES1`, `ES2`, ..., `ESN`) e contengono il suo nome e cognome.
Un possibile esempio del contenuto del file `dati_lingotto.csv` è il seguente:

```file
ST1,9,1,150
ST2,12,2,220,3
ES1,Marco,Rossi
ST3,6,1,180,Ingresso
...
```

### Prezzi degli stand
Gli stand Standard sono gli unici per i quali il prezzo corrisponde esattamente al valore indicato nel file.
Per tutte le altre tipologie di stand viene applicato un sovrapprezzo, calcolato in base alle loro
caratteristiche:

- Stand con prese elettriche aggiuntive → sovrapprezzo pari al 7% per ogni presa extra, ovvero:
`prezzo finale = prezzo base × (1 + 0.07 × numero_prese)`
- Stand Premium → sovrapprezzo fisso del 30%: `prezzo finale = prezzo base × 1.30`

In questo modo, il costo finale degli stand con prese elettriche aggiuntive cresce proporzionalmente al
numero di prese disponibili.

### Implementazione
Per questo laboratorio è necessario utilizzare la classe `LingottoFiere` presente nel file
`lingotto_fiere.py`. Le informazioni sugli stand devono essere modellate tramite classi dedicate. Il file
`main.py` consente di interagire con il sistema tramite un menù testuale utilizzabile dalla console.

```menu in console
--- MENU LINGOTTO FIERE ---
1. Modifica nome del centro fieristico
2. Carica dati da file
3. Assegna stand a espositore
4. Visualizza elenco espositori
5. Visualizza stand ordinati per prezzo
6. Esci
Scegli un'opzione >>
```

Le operazioni di gestione del sistema devono essere centralizzate all'interno della classe `LingottoFiere`,
che rappresenta l'elemento principale attraverso cui avviene ogni interazione con i dati. La modifica e la
lettura delle informazioni relative al centro, come ad esempio il nome, possono essere realizzate accedendo
direttamente agli attributi della classe oppure, in modo più strutturato, tramite metodi getter e setter
appositamente definiti.

Uno dei compiti fondamentali della classe consiste nel caricamento dei dati dal file. A questo scopo deve
essere implementato un metodo dedicato, `carica_file_dati(file_path)`, che si occupa di leggere il file e di
creare in modo automatico gli oggetti corrispondenti alle righe presenti. In particolare, le righe relative
agli stand verranno interpretate per determinare la tipologia corretta, riflettendo e sfruttando l'aspetto
dell'ereditarietà delle classi: se sono presenti solo quattro campi verrà creato uno stand Standard; se è
presente un campo numerico aggiuntivo si tratterà di uno stand con prese elettriche aggiuntive; infine, se il
campo aggiuntivo è testuale verrà generato uno stand di tipo Premium. Allo stesso modo, le righe relative agli
espositori porteranno alla creazione degli oggetti specifici. Tutti questi oggetti verranno poi memorizzati
all'interno del sistema per essere gestiti successivamente. Nel caso in cui il file non venga trovato, il
metodo dovrà sollevare un'eccezione `FileNotFoundError` per segnalare l'errore.

La classe `LingottoFiere` deve prevedere inoltre un metodo per l'assegnazione di uno stand a un espositore, chiamato 
`assegna_stand_a_espositore(codice_stand, codice_espositore)`. Quando viene effettuata una richiesta, il sistema deve 
verificare che lo stand e l'espositore esistano, che lo stand sia effettivamente disponibile e che l'espositore non sia 
già associato a un altro stand. Ogni stand deve mantenere un riferimento all'espositore a cui è stato assegnato. 
Se tutte le condizioni sono soddisfatte, lo stand viene contrassegnato come non disponibile e viene registrata 
l'associazione tra espositore e stand. Se una delle verifiche non va a buon fine, il metodo deve sollevare un'eccezione 
per segnalare l'errore.

La classe `LingottoFiere` deve avere un metodo `elenca_espositori()` che stampa l'elenco degli
espositori specificando, quando applicabile, lo stand a cui ciascun espositore è associato.

> **💡 SUGGERIMENTO:**
> Per confrontare due oggetti tramite l'operatore `==`, è possibile definire nella classe il metodo speciale 
> `__eq__(self, other)`, che permette di stabilire quando due istanze devono essere considerate uguali, ad esempio in 
> base a un codice identificativo.

Infine, per facilitare la consultazione e la scelta degli stand, la classe `LingottoFiere` deve inoltre mettere a
disposizione un metodo che permetta di visualizzare l'elenco degli stand ordinati in base al prezzo. Il
metodo `stand_ordinati_per_prezzo()` restituirà la lista degli stand partendo da quelli più economici fino a
quelli più costosi, fornendo così uno strumento utile sia per la gestione interna che per l'esperienza
dell'utente.

> **💡 SUGGERIMENTO:**
> Per ordinare una lista di oggetti tramite `sorted(lista)` o `lista.sort()`, definendo un algoritmo specifico 
> (ad esempio, più sofisticato del semplice ordinamento crescente o decrescente secondo uno dei suoi attributi, 
> quindi dell’impiego di `key=attrgetter("<attributo>")`), è possibile definire nella classe il metodo speciale 
> `__lt__(self, other)`, che permette di stabilire quando un oggetto è minore (`<`) di un altro.

> **💡 NOTA:**
> Per rendere le informazioni leggibili e chiare, tutte le classi coinvolte devono implementare un metodo
> speciale di rappresentazione testuale, come `__str__()` e/o `__repr__()`. In questo modo, quando un oggetto
> viene stampato, restituirà una descrizione comprensibile e dettagliata del suo stato. Ad esempio, la stampa
> di uno stand con prese elettriche aggiuntive potrebbe produrre un output come:
>
> ```stand stampato
> ST2: Prese Extra | 12 mq - Padiglione 2 - Prezzo 266.20€ - Prese aggiuntive: 3 - Disponibile
> ```
