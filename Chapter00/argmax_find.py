"""Chapter 0 · Trace: Finding the argmax

Loops over the payoffs of four actions to find the largest one (max) and the
action that gives it (argmax); on a tie it keeps the first one found. Identical
to the code on the slide.
"""

action = ["A", "B", "C", "D"]
payoff = [3, 7, 2, 7]
best = 0               # index of the best
for i in range(1, 4):
    if payoff[i] > payoff[best]:
        best = i
print(payoff[best], action[best])


# Expected output:
# 7 B
