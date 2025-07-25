import requests
import tkinter as tk
from tkinter import ttk

API_KEY = "1ccaeda55dbb420baa90350d"  # chiave API

history = []  # lista per lo storico delle conversioni

# creo una funzione per ottenere i tassi di cambio
def get_exchange_rates(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"  # URL per ottenere i tassi di cambio
    response = requests.get(url)  # effettuo la richiesta all'API
    data = response.json()  # converto la risposta in formato JSON
    if response.status_code == 200:  # controllo se la richiesta è andata a buon fin
        rates = data['conversion_rates']  # estraggo i tassi di cambio
        return rates[target_currency]  # ottengo il tasso di cambio per la valuta di destinazione
    else:
        raise Exception(f"Errore nell'ottenere i tassi: {data.get('error-type', 'Errore sconosciuto')}")
    
# creo una funzione per ottenere le valute disponibili
def get_currency_list():
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get("result") == "success":
            # formatta come "EUR - Euro", "USD - United States Dollar"
            codes = [f"{code} - {name}" for code, name in data["supported_codes"]]
            return sorted(codes)
        else:
            print("Errore API:", data)
            return ["EUR - Euro", "USD - United States Dollar"]
    except Exception as e:
        print("Errore nel recupero delle valute:", e)
        return ["EUR - Euro", "USD - United States Dollar"]


# creo una funzione per convertire le valute
def convert_currency(amount, base_currency, target_currency, api_key):
    rate = get_exchange_rates(api_key, base_currency, target_currency) # ottengo il tasso di cambio
    return amount * rate  # calcolo l'importo convertito

# creo una funzione pper ottenere la conversione delle valute
def on_convert_click():
    try:
        amount = float(entry_amount.get())
        base_currency = selected_from.get().split(" - ")[0] # valita di partenza
        target_currency = selected_to.get().split(" - ")[0] # valuta di destinazione
        converted = convert_currency(amount, base_currency, target_currency, API_KEY) # converto la valuta
        result_text = f"{amount} {base_currency} = {converted:.2f} {target_currency}"  # formato il risultato
        result_label.config(text=result_text) # il risultato viene aggiornato
        
        # salvo nella cronologia
        history.append(result_text)
        history_list.insert(tk.END, result_text)
    except Exception as e:
        result_label.config(text=f"❌ Errore: {e}")

# creo la funzione per resettare lo storico
def reset_history():
    history.clear() # svuoto la lista dello storico
    history_list.delete(0, tk.END) # rimuovo tutti gli elementi dalla Listbox
    result_label.config(text="📄 Storico cancellato.")

# ====== INTERFACCIA GRAFICA ======

window = tk.Tk()
window.title("Convertitore Valute 💱")
window.geometry("630x600")
window.config(bg="#f0f8ff")

# === Titolo ===
title = tk.Label(window, text="CONVERTITORE DI VALUTE", font=("Helvetica", 20, "bold"), bg="#4682b4", fg="white")
title.pack(pady=20)

# === Input dell'importo ===
label_amount = tk.Label(window, text="Importo:", font=("Helvetica", 12), bg="#f0f8ff")
label_amount.pack() # aggiungo il label per l'importo
entry_amount = tk.Entry(window, font=("Helvetica", 14))
entry_amount.insert(0, "100")
entry_amount.pack(pady=5)

# === ottengo le valute dall'API ===
currency_list = get_currency_list()

# === Selettore per la valuta di partenza ===
label_from = tk.Label(window, text="Da:", font=("Helvetica", 12), bg="#f0f8ff")
label_from.pack()
selected_from = tk.StringVar(value="EUR")
dropdown_from = ttk.Combobox(window, textvariable=selected_from, values=currency_list, state="readonly", font=("Helvetica", 12))
dropdown_from.pack(pady=5)

# === Selettore per la valuta di destinazione ===
label_to = tk.Label(window, text="A:", font=("Helvetica", 12), bg="#f0f8ff")
label_to.pack()
selected_to = tk.StringVar(value="USD")
dropdown_to = ttk.Combobox(window, textvariable=selected_to, values=currency_list, state="readonly", font=("Helvetica", 12))
dropdown_to.pack(pady=5)

# === Pulsante Converti ===
convert_button = tk.Button(window, text="Converti Ora", font=("Helvetica", 14), bg="#4caf50", fg="white", command=on_convert_click)
convert_button.pack(pady=10)

# === Risultato ===
result_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"), bg="#d1ecf1", fg="#0c5460", relief="sunken")
result_label.pack(pady=10, fill="x", padx=40) # per riempire l'area orizzontalmente

# === Storico ===
history_label = tk.Label(window, text="🕓 Storico delle conversioni:", font=("Helvetica", 12, "bold"), bg="#f0f8ff")
history_label.pack(pady=(20, 5)) 

history_list = tk.Listbox(window, width=60, height=6, font=("Courier", 10))
history_list.pack(pady=5)

# === Pulsante Reset ===
reset_button = tk.Button(window, text="🗑 Cancella Storico", font=("Helvetica", 10), bg="#e74c3c", fg="white", command=reset_history)
reset_button.pack(pady=10)

# === Avvio finestra ===
window.mainloop()
