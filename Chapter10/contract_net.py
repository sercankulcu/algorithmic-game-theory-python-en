"""Chapter 10 · Code Trace: contract_net()

Puts tasks up for bid one after another using the contract net protocol; each
task goes to the idle robot with the lowest bid. Identical to the slide code;
the example below is the 3-robot / 3-task cost table from the lecture notes.
"""


def contract_net(tasks, cost):
  free = set(cost)
  assign, total = {}, 0
  for g in tasks:
    bids = {r: cost[r][g] for r in free}
    winner = min(bids, key=bids.get)
    assign[g] = winner
    total += bids[winner]
    free.remove(winner)
  return assign, total


if __name__ == "__main__":
  cost = {
    "R1": {"G1": 2, "G2": 3, "G3": 5},
    "R2": {"G1": 3, "G2": 7, "G3": 4},
    "R3": {"G1": 6, "G2": 8, "G3": 9},
  }
  assign, total = contract_net(["G1", "G2", "G3"], cost)
  print(assign, total)

# Expected output:
# {'G1': 'R1', 'G2': 'R2', 'G3': 'R3'} 18
