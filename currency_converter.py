
import requests

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
