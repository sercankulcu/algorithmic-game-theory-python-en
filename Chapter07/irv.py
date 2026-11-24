"""Chapter 7 · Code Trace: irv()

Runs an instant-runoff (IRV) count: until a candidate has a majority, it
eliminates the candidate with the fewest votes in each round and transfers the
ballots. The function is identical to the code on the "Code Trace: irv()" slide.
"""


def irv(ballots, cands):
  remaining = list(cands)
  while True:
    tally = {a: 0 for a in remaining}
    for count, order in ballots:
      top = next(a for a in order if a in remaining)
      tally[top] += count
    leader = max(tally, key=tally.get)
    if 2 * tally[leader] > sum(tally.values()):
      return leader
    loser = min(tally, key=tally.get)
    remaining.remove(loser)


if __name__ == "__main__":
  # Main profile from the lecture notes: 13 voters, 4 candidates
  ballots = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(irv(ballots, ["A", "B", "C", "D"]))

# Expected output:
# C
