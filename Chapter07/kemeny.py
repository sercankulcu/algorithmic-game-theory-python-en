"""Chapter 7 · Code Trace: kemeny()

Tries every ordering of the candidates and returns the Kemeny ranking, the one
with the largest agreement score with the voters. The code is identical to the
"Code Trace: kemeny()" slide.
"""

from itertools import permutations
def kemeny(ballots, cands):
  best, best_score = None, -1
  for order in permutations(cands):
    score = 0
    for i, x in enumerate(order):
      for y in order[i + 1:]:
        score += sum(n for n, b in ballots
                     if b.index(x) < b.index(y))
    if score > best_score:
      best, best_score = order, score
  return best, best_score


if __name__ == "__main__":
  # Cycle profile from the lecture notes: 9 voters, 3 candidates
  cycle = [(4, "ABC"), (3, "BCA"), (2, "CAB")]
  print(kemeny(cycle, "ABC"))
  # Main profile: 13 voters, 4 candidates
  ballots = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(kemeny(ballots, "ABCD"))

# Expected output:
# (('A', 'B', 'C'), 17)
# (('D', 'B', 'C', 'A'), 44)
