"""Chapter 14 · Learning Prices from Data

From buyer values observed in the past, picks the reserve price that maximizes
the empirical revenue (the candidate prices are the sample values themselves).
Identical to the slide code; the example is the 8 buyer values from the lecture
notes.
"""

def best_price(samples):
  v = sorted(samples, reverse=True)
  n = len(v)
  price, revenue = 0, 0
  for k in range(1, n + 1):
    p = v[k - 1]        # k-th highest
    g = p * k / n       # k buyers buy
    if g > revenue:
      price, revenue = p, g
  return price, revenue


if __name__ == "__main__":
  samples = [0.62, 0.15, 0.91, 0.47, 0.33, 0.78, 0.55, 0.08]
  price, revenue = best_price(samples)
  print(price, round(revenue, 3))

# Expected output:
# 0.47 0.294
