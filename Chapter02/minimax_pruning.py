"""Chapter 2 · Code Trace: Minimax

Computes the minimax value recursively on a small two-level game tree given as a
dictionary (A → B, C, D). Identical to the code in the Minimax and Pruning deck.
"""

from math import inf
T = {"A": ["B", "C", "D"], "B": [3, 5],
     "C": [2, 9], "D": [6, 4]}
def minimax(n, maxi):
  if isinstance(n, int):        # leaf
    return n
  best = -inf if maxi else inf
  for c in T[n]:
    v = minimax(c, not maxi)
    if maxi:
      best = max(best, v)
    else:
      best = min(best, v)
  return best
print(minimax("A", True))


# Expected output:
# 4
