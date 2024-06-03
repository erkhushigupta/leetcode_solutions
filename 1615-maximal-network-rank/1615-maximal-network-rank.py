from collections import defaultdict

from typing import List


class Solution:

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # Create a graph using a dictionary, where each node points to a set of connected nodes

        graph = defaultdict(set)

      

        # Build the graph with the given list of roads

        for a, b in roads:

            graph[a].add(b)

            graph[b].add(a)

      

        # Initialize the maximum network rank to zero

        max_network_rank = 0

      

        # Check every pair of cities to find the maximal network rank

        for city_a in range(n):

            for city_b in range(city_a + 1, n):

                # Calculate the network rank for the pair (a, b), which is the sum of

                # their connected cities minus one if they are directly connected

                connected_cities = len(graph[city_a]) + len(graph[city_b])

                if city_a in graph[city_b]:

                    connected_cities -= 1

              

                # Update the maximum network rank if this pair has a higher rank

                if connected_cities > max_network_rank:

                    max_network_rank = connected_cities

      

        # Return the maximum network rank

        return max_network_rank