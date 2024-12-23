# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right


class Solution:

    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        # Function to swap elements in an array

        def swap_elements(array, i, j):

            array[i], array[j] = array[j], array[i]


        # Function to find the minimum number of swaps needed

        # to sort the array

        def find_min_swaps_to_sort(array):

            length = len(array)

            # Create a mapping from value to its index after sort

            value_to_index = {value: index for index, value in enumerate(sorted(array))}

            # Replace each value with its index after sort

            for i in range(length):

                array[i] = value_to_index[array[i]]

            swaps = 0

            # Iterate through the array, swapping elements until

            # the current index matches the sorted index

            for i in range(length):

                while array[i] != i:

                    swap_elements(array, i, array[i])

                    swaps += 1

            return swaps


        # Start with a queue containing the root node

        queue = deque([root])

        total_swaps = 0

        # Perform breadth-first traversal of the tree

        while queue:

            current_level = []

            # Process all nodes at the current level

            for _ in range(len(queue)):

                node = queue.popleft()

                # Add the node's value to the current level array

                current_level.append(node.val)

                # Add left and right children to queue if they exist

                if node.left:

                    queue.append(node.left)

                if node.right:

                    queue.append(node.right)

            # For each level, add the number of swaps needed to sort

            # the level's values to the total number of swaps

            total_swaps += find_min_swaps_to_sort(current_level)

      

        # Return the total number of swaps required for the whole tree

        return total_swaps