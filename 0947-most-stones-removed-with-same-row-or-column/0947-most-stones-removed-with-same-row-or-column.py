from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(u: int):
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    dfs(v)
        
        num_of_islands = 0
        n = len(stones)
        graph = [[] for _ in range(n)]
        seen = set()

        # Build the graph based on row and column connections
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        # Count the number of connected components
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                num_of_islands += 1

        # The number of stones we can remove is total stones minus the number of connected components
        return n - num_of_islands
