"""Chapter 5 · Double Auction Code Trace

In a double auction, sorts and matches the bids and asks and returns the number
of trades and the price found by the midpoint rule. The function is identical to
the code on the "Double Auction Code Trace" slide.
"""


def double_auction(bids, asks):
  b = sorted(bids, reverse=True)  # buyers
  s = sorted(asks)                # sellers
  k, n = 0, min(len(b), len(s))
  while k < n and b[k] >= s[k]:
    k += 1                   # pair matched
  if k == 0:
    return 0, None
  lo = max([s[k-1]] + b[k:k+1])
  hi = min([b[k-1]] + s[k:k+1])
  return k, (lo + hi) / 2


if __name__ == "__main__":
  # Example from the lecture notes: five buyers, five sellers
  bids = [70, 40, 90, 55, 80]
  asks = [60, 85, 35, 75, 50]
  print(double_auction(bids, asks))


# Expected output:
# (3, 65.0)
