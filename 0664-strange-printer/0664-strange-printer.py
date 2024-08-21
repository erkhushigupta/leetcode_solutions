class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # Initialize a 2D array with None to indicate uncomputed values
        mem = [[None] * n for _ in range(n)]
        return self._strangePrinter(s, 0, n - 1, mem)

    def _strangePrinter(self, s: str, i: int, j: int, mem: list[list[int]]) -> int:
        if i > j:
            return 0
        if mem[i][j] is not None:
            return mem[i][j]

        # Initially assume printing s[i] and then solving for the rest
        mem[i][j] = self._strangePrinter(s, i + 1, j, mem) + 1

        # Try to minimize by combining sections where s[i] matches
        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                mem[i][j] = min(mem[i][j], self._strangePrinter(s, i, k - 1, mem) +
                                               self._strangePrinter(s, k + 1, j, mem))

        return mem[i][j]
