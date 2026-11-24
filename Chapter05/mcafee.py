"""Chapter 5 · McAfee Code Trace

Applies the McAfee rule in a double auction: if the average of the first excluded
pair is acceptable, all trades happen at a single price; otherwise the last pair
is dropped and two separate prices are used. The function is identical to the
code on the "McAfee Code Trace" slide.
"""


def mcafee(bids, asks):
  b = sorted(bids, reverse=True) + [float('-inf')]
  s = sorted(asks) + [float('inf')]
  k = 0
  while b[k] >= s[k]:
    k += 1                 # efficient trade
  if k == 0: return 0, None, None
  p0 = (b[k] + s[k]) / 2   # excluded pair
  if s[k-1] <= p0 <= b[k-1]:
    return k, p0, p0       # one price
  return k - 1, b[k-1], s[k-1]  # two prices


if __name__ == "__main__":
  # The two examples from the lecture notes: first one price, then two prices
  print(mcafee([70, 40, 90, 55, 80], [60, 85, 35, 75, 50]))
  print(mcafee([90, 80, 70, 40], [30, 50, 65, 85]))


# Expected output:
# (3, 65.0, 65.0)
# (2, 70, 65)
