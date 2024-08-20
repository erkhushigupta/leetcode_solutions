class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        # suffix[i] := sum(piles[i..n))
        suffix = piles[:]
        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]
        
        # Memoization table
        mem = [[0] * (n + 1) for _ in range(n)]

        def dp(i, M):
            if i + 2 * M >= n:
                return suffix[i]
            if mem[i][M] != 0:
                return mem[i][M]
            
            # Calculate opponent's minimum possible stones
            opponent = suffix[i]
            for X in range(1, 2 * M + 1):
                opponent = min(opponent, dp(i + X, max(M, X)))
            
            mem[i][M] = suffix[i] - opponent
            return mem[i][M]
        
        return dp(0, 1)

