# PYTHON-CURRENCY-CONVERTER

Un'applicazione desktop semplice e intuitiva per convertire valute in tempo reale utilizzando l'[ExchangeRate API](https://www.exchangerate-api.com/), realizzata con **Python** e **Tkinter**.

## 🧠 Descrizione

Questa applicazione consente agli utenti di:

- Convertire importi tra diverse valute supportate.
- Visualizzare il risultato in formato leggibile.
- Tenere traccia dello storico delle conversioni.
- Cancellare facilmente lo storico.

L'interfaccia grafica è costruita con **Tkinter**, mentre per i dati dei tassi di cambio viene utilizzata una chiamata HTTP verso un'API esterna.

---

## 🛠️ Tecnologie Utilizzate

- **Python 3**
- **Tkinter** – per la GUI
- **requests** – per le chiamate HTTP all'API
- **ExchangeRate API** – per i tassi di cambio in tempo reale

---

## 🚀 Come Avviare il Progetto

### ✅ Prerequisiti

Assicurati di avere Python installato (versione 3.x). Installa il modulo `requests`:

```bash
pip install requests
```

## ▶️ Esecuzione

- Clona o scarica questa repository
- Apri il file ed esegui lo script con:

```bash
python currency_converter.py
```