
import requests
import tkinter as tk

history = [] 

# creo una funzione per ottenere i tassi di cambio dall'API
def get_exchange_rates(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"  # creo l'URL per la richiesta all'API
    response = requests.get(url) # invio la richiesta GET all'API
    data = response.json() # converto la risposta in formato JSON
    if response.status_code == 200: # controllo se la richiesta è andata a buon fine
        rates = data['conversion_rates'] # estraggo i tassi di cambio dalla risposta
        return rates[target_currency] # restituisco il tasso di cambio per la valuta di destinazione
    else:
        raise Exception(f"Errore nell'ottenere i tassi di cambio: {data['error-type']}")
    
# creo una funzione per convertire l'importo delle valute
def convert_currency(amount, base_currency, target_currency, api_key):
    rate = get_exchange_rates(api_key, base_currency, target_currency) # ottengo il tasso di cambio
    converted_amount = amount * rate # calcolo l'importo convertito
    return converted_amount # restituisco l'importo convertito


# Funzione per resettare lo storico
def reset_history():
    history.clear() # pulisco la lista dei risultati
    history_list.delete(0, tk.END) # pulisco la lista dello storico
    result_label.config(text="📄 Storico cancellato.")

def main():
    api_key = "1ccaeda55dbb420baa90350d"
    print("CONVERTITORE DI VALUTE")

    while True:
        try:
            amount = float(input("Inserisci l'importo da convertire: "))
            base_currency = input("Inserisci la valuta di partenza (es. EUR): ").upper()
            target_currency = input("Inserisci la valuta di destinazione (es. USD): ").upper()  
            converted_amount = convert_currency(amount, base_currency, target_currency, api_key) # converto l'import
            print(f"{amount} {base_currency} corrispondono a {converted_amount:.2f} {target_currency}") 
        except Exception as e:  
            print(f"Errore: {e}")

        another = input("Vuoi convertire un altro importo? (s/n): ").lower()
        if another != 's':      
            print("Grazie per aver usato il convertitore di valute!")
            break

if __name__ == "__main__":
    main()

# Interfaccia grafica con tkinter
window = tk.Tk()
window.title("Simulatore Lancio di Dadi") # Titolo
window.geometry("630x600") # Dimensioni
window.config(bg="#3012d8") # Colore sfondo 

# Titolo
title = tk.Label(window, text="CONVERTITORE VALUTE 💰", font=("Helvetica", 18, "bold"), bg="#e71c1c") # stile CSS 
title.pack(pady=10) # Spaziatura verticale (padding)

# Pulsante lancio
launch_button = tk.Button(window, text=" Ottieni Importo!", font=("Helvetica", 14), bg="#27ae60", fg="white", activebackground="#1e8449")
launch_button.pack(pady=10)

# Risultato corrente
result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#13eb62")
result_label.pack(pady=5)

# Sezione storico
history_label = tk.Label(window, text="🕓 Storico delle conversioni:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
history_label.pack()

history_list = tk.Listbox(window, width=60, height=6, font=("Courier", 10))
history_list.pack(pady=5)

# === Separatore visivo ===
separator = tk.Frame(window, height=2, bd=1, relief="sunken", bg="#fffafa")
separator.pack(fill="x", padx=20, pady=10)

# Pulsante reset
reset_button = tk.Button(window, text="🗑 Cancella Storico", font=("Helvetica", 10), bg="#e74c3c", fg="white", activebackground="#c0392b", command=reset_history)
reset_button.pack(pady=5)

# Avvio il lopp principale dell'interfaccia grafica
window.mainloop()