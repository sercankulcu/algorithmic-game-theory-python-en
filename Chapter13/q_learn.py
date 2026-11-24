"""Chapter 13 · Code Trace: Q-learning

Applies the Q-learning update to recorded episodes in a four-cell corridor
(s3 is the goal, r = 1). Identical to the slide code; the example is the three
episodes and the call q_learn(ep, 0.5, 0.9) from the lecture notes.
Action 0 = left, 1 = right.
"""

def q_learn(episodes, alpha, gamma):
    Q = [[0.0, 0.0] for s in range(4)]  # [left, right]
    for ep in episodes:
        for s, a, r, s2 in ep:
            best = 0 if s2 == 3 else max(Q[s2])
            target = r + gamma * best
            Q[s][a] += alpha * (target - Q[s][a])
    return Q


if __name__ == "__main__":
    right = [(0, 1, 0, 1), (1, 1, 0, 2), (2, 1, 1, 3)]
    detour = [(0, 1, 0, 1), (1, 0, 0, 0), (0, 1, 0, 1), (1, 1, 0, 2), (2, 1, 1, 3)]
    ep = [right, right, detour]
    Q = q_learn(ep, 0.5, 0.9)
    for s in range(3):
        print("s%d" % s, [round(x, 3) for x in Q[s]])

# Expected output:
# s0 [0.0, 0.152]
# s1 [0.046, 0.45]
# s2 [0.0, 0.875]
