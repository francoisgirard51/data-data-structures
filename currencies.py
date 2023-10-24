# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
    "EURUSD": 1.17
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    value, source_currency = amount
    conversion_rate_key = source_currency + currency

    if conversion_rate_key in RATES:
        rate = RATES[conversion_rate_key]
        converted_amount = round(value * rate)
        return converted_amount

    return None
