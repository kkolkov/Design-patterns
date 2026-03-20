from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    
    @abstractmethod
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        pass