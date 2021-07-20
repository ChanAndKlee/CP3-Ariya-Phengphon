from forex_python.converter import CurrencyRates
c = CurrencyRates()
result = c.get_rates('USD')   # you can directly call get_rates('USD')
print(result)