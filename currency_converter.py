
import requests

# creo una funzione per ottenere i tassi di cambio dall'API
def get_exchange_rates(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        rates = data['conversion_rates']
        return rates[target_currency]
    else:
        raise Exception(f"Errore nell'ottenere i tassi di cambio: {data['error-type']}")
    
# creo una funzione per convertire l'importo delle valute
def convert_currency(amount, base_currency, target_currency, api_key):
    rate = get_exchange_rates(api_key, base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount

def main():
    api_key = "1ccaeda55dbb420baa90350d"
    print("CONVERTITORE DI VALUTE")
    