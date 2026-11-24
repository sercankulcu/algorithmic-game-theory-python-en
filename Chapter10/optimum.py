"""Chapter 10 · Code Trace: optimum()

A center that knows all the costs finds the cheapest assignment by trying every
ordering of the robots. Identical to the slide code; the
`from itertools import permutations` line, which is not visible on the slide,
is added.
"""
from itertools import permutations   # not on the slide; added so the code runs


def optimum(tasks, cost):
  best = None
  for p in permutations(cost):
    t = sum(cost[r][g]
            for g, r in zip(tasks, p))
    if best is None or t < best[0]:
      best = (t, p)
  return best


if __name__ == "__main__":
  cost = {
    "R1": {"G1": 2, "G2": 3, "G3": 5},
    "R2": {"G1": 3, "G2": 7, "G3": 4},
    "R3": {"G1": 6, "G2": 8, "G3": 9},
  }
  print(optimum(["G1", "G2", "G3"], cost))

# Expected output:
# (13, ('R3', 'R1', 'R2'))
