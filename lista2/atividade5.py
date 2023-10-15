class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.rates or to_currency not in self.rates:
            return None
        if amount <= 0:
            return None
        if from_currency == to_currency:
            return amount
        exchange_rate = self.rates[to_currency] / self.rates[from_currency]
        converted_amount = amount * exchange_rate
        return converted_amount

rates = {
    "USD": 1.0,
    "BRL": 5.5,
    "EUR": 0.85,
    "JPY": 110.0
}

converter = CurrencyConverter(rates)

from_currency = input("Insira a moeda que deseja converter: ")
to_currency = input("Insira a moeda qual deseja converter para: ")
amount = float(input("Insira a quantidade que deseja converter: "))

converted_amount = converter.convert(from_currency, to_currency, amount)
if converted_amount is None:
    print("Não foi possível realizar a conversão.")
else:
    print(f"{amount} {from_currency} é igual a {converted_amount:.2f} {to_currency}")