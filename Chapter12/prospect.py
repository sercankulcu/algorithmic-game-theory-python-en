"""Chapter 12 · Code Trace: prospect()

Uses the value function of prospect theory (α = 0.88, λ = 2.25) to compute the
value of 50-50 bets of +G / −100 and shows when the bet is accepted. Identical
to the slide code.
"""

def v(x):
    if x >= 0: return x ** 0.88
    return -2.25 * (-x) ** 0.88
def prospect(G, K):      # ½: +G, ½: −K
    return 0.5 * v(G) + 0.5 * v(-K)
for G in [100, 200, 251, 300]:
    print(G, round(prospect(G, 100), 1))

# Expected output:
# 100 -36.0
# 200 -11.8
# 251 -0.1
# 300 10.9
