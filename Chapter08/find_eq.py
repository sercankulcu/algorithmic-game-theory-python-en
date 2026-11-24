"""Chapter 8 · Code Trace: find_eq

Searches for the Wardrop equilibrium of a network with two parallel routes by
bisection: it narrows the number of cars on Route 1 until the delays of the two
routes are equal. The function is identical to the code on the "Code Trace:
find_eq" slide.
"""


def find_eq(l1, l2, r, eps=50):
  lo, hi = 0, r
  while hi - lo > eps:
    x = (lo + hi) / 2
    if l1(x) < l2(r - x):
      lo = x      # Route 1 still faster: raise
    else:
      hi = x      # Route 1 slower: lower
  return (lo + hi) / 2


if __name__ == "__main__":
  # Example from the lecture notes: 3,000 cars, l1 = 5 + x/100, l2 = 20 + x/200
  route1 = lambda x: 5 + x / 100
  route2 = lambda x: 20 + x / 200
  print(round(find_eq(route1, route2, 3000), 2))
  # Example 8.7: 6,000 cars, l1 = 10 + x/200, l2 = 25 + x/100
  route1 = lambda x: 10 + x / 200
  route2 = lambda x: 25 + x / 100
  print(round(find_eq(route1, route2, 6000), 2))

# Expected output:
# 1992.19
# 4992.19
