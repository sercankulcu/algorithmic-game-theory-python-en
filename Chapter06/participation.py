"""Chapter 6 · Code Trace: participation

On a two-sided platform with fixed prices, simulates buyers and sellers reacting
to each other in turn and returns the participation (in thousands of people)
after a few rounds. The function is identical to the code on the
"Code Trace: participation" slide.
"""


def participation(pA, pB, rounds=8):
  nA, nB = 0, 0
  for t in range(rounds):
    nA = 20 + 0.25 * nB - pA   # buyers
    nB = 80 + 0.75 * nA - pB   # sellers
  return nA, nB


if __name__ == "__main__":
  # Example from the lecture notes: optimal prices pA = -5, pB = 50
  nA, nB = participation(-5, 50)
  print(round(nA, 1), round(nB, 1))
  print("profit:", round(-5 * nA + 50 * nB, 1))


# Expected output:
# 40.0 60.0
# profit: 2800.0
