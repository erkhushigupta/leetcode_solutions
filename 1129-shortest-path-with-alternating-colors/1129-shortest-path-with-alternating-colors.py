from collections import deque, defaultdict

from typing import List


class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        # Create adjacency lists for red and blue edges separately using default dictionaries

        graph = [defaultdict(list) for _ in range(2)]

        for start, end in red_edges:

            graph[0][start].append(end)

        for start, end in blue_edges:

            graph[1][start].append(end)


        # Initialize the answer list with -1, indicating unreachable nodes

        distances = [-1] * n

        # Initialize a set to keep track of visited (node, color) pairs

        visited = set()

        # Doubly-ended queue to store the current node and the color of the edge used to reach it

        queue = deque([(0, 0), (0, 1)])

        # Distance from the source node (node 0)

        distance = 0


        # Iterate until there are no more nodes to visit

        while queue:

            for _ in range(len(queue)):

                # Pop the node and its edge color from the queue

                node, color = queue.popleft()

                # If this node's distance hasn't been set yet, set it to the current distance

                if distances[node] == -1:

                    distances[node] = distance

                # Mark this (node, color) as visited

                visited.add((node, color))

                # Alternate the color for the next edges to consider (0 -> 1 or 1 -> 0)

                color ^= 1

                # Enqueue all the adjacent nodes of the alternated color

                for neighbor in graph[color][node]:

                    if (neighbor, color) not in visited:

                        queue.append((neighbor, color))

            # After exploring the nodes at the current distance, increment for the next level

            distance += 1


        # Return the list of minimum distances to each node

        return distances