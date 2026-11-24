"""Chapter 5 · Shading Code Trace

In a first-price auction, when rivals bid (n - 1)/n times their values, searches
a grid by brute force for the bid that maximizes expected utility. The function
is identical to the code on the "Shading Code Trace" slide.
"""


def best_bid(v, n, step=0.1):
  beta = (n - 1) / n        # rivals bid beta*v
  best, b_best = -1, 0
  b = 0.0
  while b <= v:
    p = min(1, b / beta) ** (n - 1)  # P(win)
    eu = (v - b) * p
    if eu > best:
      best, b_best = eu, b
    b = round(b + step, 10)
  return b_best, best


if __name__ == "__main__":
  # Example from the lecture notes: value v = 0.8, two bidders
  bid, utility = best_bid(0.8, 2)
  print(bid, round(utility, 3))


# Expected output:
# 0.4 0.32
