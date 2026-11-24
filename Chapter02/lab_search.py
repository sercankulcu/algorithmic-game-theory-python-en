"""Chapter 2 · Search in the Lab

The depth-limited alpha-beta search from the lab and best_move, which picks the
best move at the root. Both functions are identical to the code on the slide
(there it is for Connect Four). To make them runnable, a small tic-tac-toe state
class (is_over, utility, moves, play), a simple evaluation E and order were
added; this scaffolding is not on the slide. utility is ±(1000 − k) or 0 as on
the slide (k: moves played so far).
"""

from math import inf   # not shown on the slide; needed for inf

def alphabeta(s, d, a, b, maxi):
  if s.is_over():              # game over
    return s.utility()         # ±(1000 − k) or 0
  if d == 0:
    return E(s)                # evaluation
  best = -inf if maxi else inf
  for m in order(s.moves()):
    v = alphabeta(s.play(m), d-1, a, b, not maxi)
    if maxi:
      best = max(best, v); a = max(a, best)
    else:
      best = min(best, v); b = min(b, best)
    if a >= b:
      break
  return best


def best_move(s, d):       # root: MAX
  a, top = -inf, None
  for m in order(s.moves()):
    v = alphabeta(s.play(m), d-1,
                  a, inf, False)
    if v > a:
      a, top = v, m
  return top


# ---------------------------------------------------------------------------
# Everything below is not on the slide: the smallest scaffolding needed to run
# the two functions on a small real game (tic-tac-toe).
# ---------------------------------------------------------------------------

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


class TicTacToe:
    """The board is a 9-character string: 'X', 'O' or '.' (empty); squares 0..8."""

    def __init__(self, board="........."):
        self.board = board

    def turn(self):
        return "X" if self.board.count("X") == self.board.count("O") else "O"

    def winner(self):
        for a, b, c in LINES:
            if self.board[a] != "." and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_over(self):
        return self.winner() is not None or "." not in self.board

    def utility(self):
        k = 9 - self.board.count(".")   # number of moves played
        w = self.winner()
        if w == "X":
            return 1000 - k
        if w == "O":
            return -(1000 - k)
        return 0

    def moves(self):
        return [i for i in range(9) if self.board[i] == "."]

    def play(self, m):
        t = self.board
        return TicTacToe(t[:m] + self.turn() + t[m + 1:])


def E(s):
    # lines X can still complete − lines O can still complete
    x = sum(1 for c in LINES if all(s.board[i] != "O" for i in c))
    o = sum(1 for c in LINES if all(s.board[i] != "X" for i in c))
    return x - o


PRIORITY = [4, 0, 2, 6, 8, 1, 3, 5, 7]   # center first, then corners, then edges


def order(moves):
    return sorted(moves, key=PRIORITY.index)


if __name__ == "__main__":
    # At the root it is always X's turn (MAX); utility is from X's point of view.
    for board, d in [(".........", 9), (".........", 2),
                     ("XX.OO....", 9), ("X...O...X", 9)]:
        s = TicTacToe(board)
        if s.turn() == "O":          # O plays a corner so that it is X's turn at the root
            s = s.play(2)
        print(s.board, "d =", d, "-> move", best_move(s, d),
              "value", alphabeta(s, d, -inf, inf, True))


# Expected output:
# ......... d = 9 -> move 4 value 0
# ......... d = 2 -> move 4 value 1
# XX.OO.... d = 9 -> move 2 value 995
# X.O.O...X d = 9 -> move 6 value 993
