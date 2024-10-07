def currency_converter():
    rates = {
        "EURO": {"DOLLAR": 1.10, "PKR": 315.50},
        "DOLLAR": {"EURO": 0.91, "PKR": 287.50},
        "PKR": {"EURO": 0.0032, "DOLLAR": 0.0035},
    }

    # Convert user input to uppercase to match dictionary keys
    from_currency = input("Enter the currency you have (Euro, Dollar, PKR): ").upper()
    to_currency = input("Enter the currency you want to convert to (Euro, Dollar, PKR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    if from_currency in rates and to_currency in rates[from_currency]:
        converted_amount = amount * rates[from_currency][to_currency]
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency or conversion not supported.")

currency_converter()
