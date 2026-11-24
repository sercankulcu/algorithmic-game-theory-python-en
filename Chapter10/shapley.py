"""Chapter 10 · Code Trace: shapley() (1/2 and 2/2)

Computes the Shapley value as the average of the marginal contributions over
all arrival orders. Identical to the code on both slides (the same function);
the `from itertools import permutations` line, which is not visible on the
slides, is added. The example is the game from the lecture notes with v(A)=10,
v(B)=20, v(C)=30, v(AB)=50, v(AC)=60, v(BC)=70, v(ABC)=120.
"""
from itertools import permutations   # not on the slide; added so the code runs


def shapley(N, v):
  phi = {i: 0 for i in N}
  orders = list(permutations(N))
  for order in orders:
    S = frozenset()
    for i in order:
      gain = v[S | {i}] - v[S]
      phi[i] += gain
      S = S | {i}
  return {i: phi[i] / len(orders) for i in N}


if __name__ == "__main__":
  v = {
    frozenset(): 0,
    frozenset({"A"}): 10, frozenset({"B"}): 20, frozenset({"C"}): 30,
    frozenset({"A", "B"}): 50, frozenset({"A", "C"}): 60,
    frozenset({"B", "C"}): 70,
    frozenset({"A", "B", "C"}): 120,
  }
  print(shapley(["A", "B", "C"], v))

# Expected output:
# {'A': 30.0, 'B': 40.0, 'C': 50.0}
