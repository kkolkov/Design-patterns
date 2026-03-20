from converters import UsdConverter

def main():
    try:
        amount = float(input('Введите значение в USD: \n'))
        
        converter = UsdConverter()
        
        currencies = [('RUB', 'RUB'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('CNY', 'CNY')]
        
        for code, name in currencies:
            result = converter.convert(amount, to_currency=code)
            print(f"{amount} USD to {name}: {result:.2f}")
            
    except ValueError as e:
        print(f"Ошибка: {e}")
    except RuntimeError as e:
        print(f"Ошибка API: {e}")

if __name__ == "__main__":
    main()