"""Chapter 7 · Code Trace: borda()

Adds up the Borda scores from the rankings of voter groups and returns the
candidate with the highest score. The function is identical to the code on the
"Code Trace: borda()" slide.
"""


def borda(ballots):
  score = {}
  for count, order in ballots:
    m = len(order)
    for k, cand in enumerate(order):
      p = count * (m - 1 - k)
      score[cand] = score.get(cand, 0) + p
  winner = max(score, key=score.get)
  return winner, score


if __name__ == "__main__":
  # Main profile from the lecture notes: 13 voters, 4 candidates
  ballots = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(borda(ballots))

# Expected output:
# ('B', {'A': 18, 'D': 21, 'B': 22, 'C': 17})
