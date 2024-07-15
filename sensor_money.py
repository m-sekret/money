import random

def get_currency_prices():
    return {
        "USD": round(random.uniform(27.0, 28.0), 2),
        "UAH": round(random.uniform(0.035, 0.037), 5),
        "GBP": round(random.uniform(35.0, 37.0), 2)
    }

