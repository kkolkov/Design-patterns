from .currency_converter import CurrencyConverter
from .rate_provider import ExchangeRateProvider

class UsdConverter(CurrencyConverter):
    def __init__(self, rate_provider=None):
        self._rate_provider = rate_provider or ExchangeRateProvider()
        self._rates = None
    
    def _ensure_rates(self):
        if self._rates is None:
            self._rates = self._rate_provider.get_rates()
        return self._rates
    
    def convert(self, amount: float, from_currency: str = "USD", to_currency: str) -> float:
        if from_currency.upper() != "USD":
            raise ValueError("Currently only USD conversions are supported")
        
        rates = self._ensure_rates()
        if not rates:
            raise RuntimeError("Unable to fetch exchange rates")
        
        target = to_currency.upper()
        if target not in rates:
            raise ValueError(f"Unknown currency: {to_currency}")
        
        return amount * rates[target]