# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        # Inner function to perform depth-first search (DFS) on the tree.

        def dfs(node: TreeNode, max_val: int):

            # Base case: if the current node is None, return from the function.

            if node is None:

                return

          

            # Using nonlocal keyword to modify the 'good_nodes_count'

            # variable defined in the parent function's scope

            nonlocal good_nodes_count

          

            # If the current node's value is greater than or equal

            # to the max value encountered so far, it is a 'good' node.

            if max_val <= node.val:

                # Increment count of 'good' nodes.

                good_nodes_count += 1

                # Update max value to current node's value.

                max_val = node.val

          

            # Recursively call dfs for the left child with updated max value.

            dfs(node.left, max_val)

            # Recursively call dfs for the right child with updated max value.

            dfs(node.right, max_val)


        # Initialize count of 'good' nodes to 0.

        good_nodes_count = 0

        # Invoke dfs with the root of the tree and a very small initial max value.

        dfs(root, float('-inf'))

        # Return final count of 'good' nodes.

        return good_nodes_count