import pandas as pd
import os

WOOD_MULTIPLIERS = {
    "Maple": 1.2,
    "Oak": 1.5,
    "Walnut": 2.5,
    "Pine": 1.0,
    "Reclaimed/Live Edge": 3.0
}

def calculate_price(product_type, length, width, height, wood_type):
    base_prices = {"Table": 500, "Shelf": 100, "Cutting Board": 45, "Furniture": 300}
    
    volume = length * width * height
    cost_per_ci = 0.10 # $0.10 per cubic inch
    
    multiplier = WOOD_MULTIPLIERS.get(wood_type, 1.0)
    total = (base_prices.get(product_type, 50) + (volume * cost_per_ci)) * multiplier
    return round(total, 2)

def save_order(order_data):
    file = 'orders.csv'
    df = pd.DataFrame([order_data])
    if not os.path.isfile(file):
        df.to_csv(file, index=False)
    else:
        df.to_csv(file, mode='a', header=False, index=False)