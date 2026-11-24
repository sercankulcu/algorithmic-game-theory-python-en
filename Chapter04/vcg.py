"""Chapter 4 · VCG Code Trace / VCG Single-Item Trace

The VCG mechanism: picks the outcome that maximizes total welfare and charges
each player the externality imposed on the others. The function is the same on
both slides (VCG Code Trace and VCG Single-Item Trace); the block below runs both
examples: a public project and a single item (VCG = Vickrey second-price auction).
"""

def vcg(v, A):
  N = list(v)            # players
  def w(a, S):           # welfare of S at a
    return sum(v[i][a] for i in S)
  x = max(A, key=lambda a: w(a, N))
  p = {}
  for i in N:
    D = [j for j in N if j != i]
    w_out = max(w(a, D) for a in A)  # i absent
    w_in = w(x, D)                  # i present
    p[i] = w_out - w_in
  return x, p


if __name__ == "__main__":
    # 1) Public project: P = Park, L = Library, G = Gym
    v = {'Ayşe': {'P': 40, 'L': 5, 'G': 0},
         'Bora': {'P': 0, 'L': 30, 'G': 20},
         'Cem': {'P': 10, 'L': 20, 'G': 45}}
    A = ['P', 'L', 'G']
    x, p = vcg(v, A)
    print(x, p, "total", sum(p.values()))

    # 2) Single item: outcome = who gets the item
    values = {'Ayşe': 70, 'Bora': 55, 'Cem': 85}
    v = {i: {a: (values[i] if a == i else 0) for a in values}
         for i in values}
    A = list(values)
    x, p = vcg(v, A)
    print(x, p)


# Expected output:
# G {'Ayşe': 0, 'Bora': 5, 'Cem': 20} total 25
# Cem {'Ayşe': 0, 'Bora': 0, 'Cem': 70}
