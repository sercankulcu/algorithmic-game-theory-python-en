"""Chapter 13 · Code Trace: match()

Compares two strategies over T rounds in the repeated Prisoner's Dilemma
(C = cooperate, D = defect). Identical to the slide code; the examples are the
call match(tft, stft, 6) from the lecture notes and the ten-round match of TFT
against Suspicious TFT.
"""

PAY = {"CC": (3, 3), "CD": (0, 5),
       "DC": (5, 0), "DD": (1, 1)}
tft = lambda me, opp: opp[-1] if opp else "C"
stft = lambda me, opp: opp[-1] if opp else "D"
def match(s1, s2, T):
    h1, h2, p1, p2 = [], [], 0, 0
    for t in range(T):
        a, b = s1(h1, h2), s2(h2, h1)
        u, v = PAY[a + b]
        h1.append(a); h2.append(b)
        p1, p2 = p1 + u, p2 + v
    return p1, p2


if __name__ == "__main__":
    print(match(tft, stft, 6))
    print(match(tft, stft, 10))

# Expected output:
# (15, 15)
# (25, 25)
