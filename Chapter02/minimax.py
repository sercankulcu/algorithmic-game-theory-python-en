"""Chapter 2 · Code Trace: Minimax

Computes the minimax value recursively on a two-level game tree with three
branches. Identical to the code in the Games and Representations deck (it uses
a different tree from minimax_pruning.py in the Minimax and Pruning deck).
"""

T = {"A": ["B", "C", "D"], "B": [3, 12, 8],
     "C": [2, 4, 6], "D": [14, 5, 2]}
def minimax(n, maxi):
  if isinstance(n, int):         # leaf
    return n
  best = float("-inf") if maxi else float("inf")
  for c in T[n]:
    v = minimax(c, not maxi)
    best = max(best, v) if maxi else min(best, v)
  return best
print(minimax("A", True))


# Expected output:
# 3
