"""Chapter 10 · Code Trace: power_index()

Computes the Shapley–Shubik power index in a weighted voting game by counting,
over every arrival order, the player who pushes the total past the quota (the
pivot). Identical to the slide code; the `from itertools import permutations`
line, which is not visible on the slide, is added. Examples: the parliament
[51; 50, 49, 1] from the lecture notes and the 1958 EEC Council of Ministers
[12; 4, 4, 4, 2, 2, 1].
"""
from itertools import permutations   # not on the slide; added so the code runs


def power_index(N, w, q):
  pivots = {i: 0 for i in N}
  orders = list(permutations(N))
  for order in orders:
    total = 0
    for i in order:
      total += w[i]
      if total >= q:
        pivots[i] += 1
        break
  return {i: pivots[i] / len(orders) for i in N}


if __name__ == "__main__":
  print(power_index(["A", "B", "C"], {"A": 50, "B": 49, "C": 1}, 51))
  eec = {"FR": 4, "DE": 4, "IT": 4, "BE": 2, "NL": 2, "LU": 1}
  g = power_index(list(eec), eec, 12)
  print({i: round(x, 4) for i, x in g.items()})

# Expected output:
# {'A': 0.6666666666666666, 'B': 0.16666666666666666, 'C': 0.16666666666666666}
# {'FR': 0.2333, 'DE': 0.2333, 'IT': 0.2333, 'BE': 0.15, 'NL': 0.15, 'LU': 0.0}
