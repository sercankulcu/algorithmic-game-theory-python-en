"""Chapter 0 · Trace: Expected Value of a Lottery

Computes the expected prize of a lottery with three outcomes as the sum of
prize · probability, then subtracts the 12 TL ticket price to print the net
expected gain. Identical to the code on the slide.
"""

prize = [100, 20, 0]          # TL
prob = [0.05, 0.25, 0.70]
E = 0
for i in range(3):
    E = E + prize[i] * prob[i]
print("E =", E)
print("net =", E - 12)  # ticket 12 TL


# Expected output:
# E = 10.0
# net = -2.0
