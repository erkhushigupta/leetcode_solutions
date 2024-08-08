from typing import List
class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:

        # Initialize the answer list with the starting cell

        result = [[r_start, c_start]]

      

        # If there's only one cell, return it immediately

        if rows * cols == 1:

            return result

      

        # 'k' represents the number of steps we take in a given direction before turning

        # It starts at 1 and gets incremented after finishing an east and north pass

        k = 1

      

        # Continue generating the spiral pattern until we've filled the result with all cells

        while True:

            # Each iteration goes in the pattern: East, South, West, North

            # 'dr' and 'dc' represent the change to rows and cols respectively

            # 'dk' represents how many steps we take in each direction before turning

            for dr, dc, dk in [[0, 1, k], [1, 0, k], [0, -1, k + 1], [-1, 0, k + 1]]:

                # Repeat the movement 'dk' times for the current orientation

                for _ in range(dk):

                    # Update the current position

                    r_start += dr

                    c_start += dc

                    # If we're still within the bounds of the matrix, add to result

                    if 0 <= r_start < rows and 0 <= c_start < cols:

                        result.append([r_start, c_start])

                        # If the result is now filled with all matrix cells, return it

                        if len(result) == rows * cols:

                            return result

            # Increment 'k' for the next spiral arm to have the correct step count 

            k += 2

 
