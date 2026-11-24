"""Chapter 12 · Code Trace: cascade()

Information cascade with two urns: once the a − b difference inferred from the
earlier guesses reaches 2, a person ignores her own signal. Identical to the
slide code; the example is the signal sequence a, a, b, b, b, b from the
lecture notes (the true urn is B).
"""

def cascade(signals):
    f = 0                  # a − b inferred from guesses
    guesses = []
    for s in signals:
        if f >= 2: t = 'A'     # A cascade
        elif f <= -2: t = 'B'  # B cascade
        else:
            t = 'A' if s == 'a' else 'B'
            f += 1 if s == 'a' else -1
        guesses.append(t)
    return guesses


if __name__ == "__main__":
    print(cascade(['a', 'a', 'b', 'b', 'b', 'b']))

# Expected output:
# ['A', 'A', 'A', 'A', 'A', 'A']
