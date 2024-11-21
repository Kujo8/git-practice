prices = [150, 200, 350, 120, 500, 100]

adjusted_prices = map(lambda p: p * 0.90 if p >= 300 else p, prices)

print(list(adjusted_prices))
