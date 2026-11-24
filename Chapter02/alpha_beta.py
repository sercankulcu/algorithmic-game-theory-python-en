"""Chapter 2 · Code Trace: Alpha-Beta

Runs minimax search with alpha-beta pruning on the same small tree; C's second
leaf is pruned and the result equals plain minimax. Identical to the code in the
Minimax and Pruning deck.
"""

from math import inf
T = {"A": ["B", "C", "D"], "B": [3, 5],
     "C": [2, 9], "D": [6, 4]}
def alphabeta(n, a, b, maxi):
  if isinstance(n, int):        # leaf
    return n
  best = -inf if maxi else inf
  for c in T[n]:
    v = alphabeta(c, a, b, not maxi)
    if maxi:
      best = max(best, v); a = max(a, best)
    else:
      best = min(best, v); b = min(b, best)
    if a >= b:
      break                  # cutoff
  return best
print(alphabeta("A", -inf, inf, True))


# Expected output:
# 4
