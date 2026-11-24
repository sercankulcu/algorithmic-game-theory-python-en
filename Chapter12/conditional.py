"""Chapter 12 · Code Trace: conditional()

In the public goods game, follows the round-by-round erosion of contributions
with one free rider (P1) and three conditional cooperators (who contribute the
average of the others' contributions in the previous round). Identical to the
slide code; the example is the call conditional([0, 10, 10, 10], 5) from the
lecture notes. The payoff u = 10 − k + 0.4·Σk is computed in the main block (not
on the slide).
"""

def conditional(c, rounds):
  history = [c]
  for t in range(rounds):
    new = [0]                   # P1 always free-rides
    for i in range(1, len(c)):
      others = sum(c) - c[i]
      new.append(others / (len(c) - 1))
    c = new
    history.append(c)
  return history


if __name__ == "__main__":
  for t, c in enumerate(conditional([0, 10, 10, 10], 5)):
    u = [10 - k + 0.4 * sum(c) for k in c]
    print(t, [round(k, 1) for k in c], round(u[0], 1), round(u[1], 1))

# Expected output:
# 0 [0, 10, 10, 10] 22.0 12.0
# 1 [0, 6.7, 6.7, 6.7] 18.0 11.3
# 2 [0, 4.4, 4.4, 4.4] 15.3 10.9
# 3 [0, 3.0, 3.0, 3.0] 13.6 10.6
# 4 [0, 2.0, 2.0, 2.0] 12.4 10.4
# 5 [0, 1.3, 1.3, 1.3] 11.6 10.3
