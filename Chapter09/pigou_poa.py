"""Chapter 9 · Code Trace: pigou_poa(p)

Computes the Price of Anarchy (equilibrium cost / optimum cost) in the Pigou
network whose top route has delay x**p and whose bottom route has delay 1, and
prints it for p = 1, 2, 4, 8, 16. The code is identical to the "Code Trace:
pigou_poa(p)" slide.
"""

def pigou_poa(p):          # top x**p, bottom 1
  x = (p + 1) ** (-1 / p)  # where C'(x) = 0
  opt = x ** (p + 1) + (1 - x)
  return 1 / opt           # eq. cost is 1

for p in [1, 2, 4, 8, 16]:
  print(p, round(pigou_poa(p), 3))

# Expected output:
# 1 1.333
# 2 1.626
# 4 2.151
# 8 3.081
# 16 4.727
