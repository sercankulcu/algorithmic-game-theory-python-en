"""Chapter 2 · Code Trace: Nim XOR

Computes the nim-sum (XOR) of the heaps in the game of Nim, then finds and plays
the winning move that makes the sum 0. Identical to the code on the slide.
"""

heaps = [3, 4, 5]
x = 0
for h in heaps:
    x ^= h            # nim-sum (XOR)
for i, h in enumerate(heaps):
    if h ^ x < h:     # can it shrink?
        heaps[i] = h ^ x
        print("heap", i, ":", h, "->", h ^ x)
        break
print(heaps)


# Expected output:
# heap 0 : 3 -> 1
# [1, 4, 5]
