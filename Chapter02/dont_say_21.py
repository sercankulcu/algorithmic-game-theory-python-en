"""Chapter 2 · Code Trace: Don't Say 21

In the game Don't Say 21, labels every number as winning or losing by backward
labeling and prints the key numbers (the losing positions). Identical to the
code on the slide.
"""

TARGET = 21
wins = {TARGET - 1: False}   # c=20: lost
for c in range(TARGET - 2, -1, -1):
    wins[c] = any(not wins[c + k]
        for k in (1, 2, 3) if c + k < TARGET)
keys = [c for c in wins if not wins[c]]
print(sorted(keys))


# Expected output:
# [0, 4, 8, 12, 16, 20]
