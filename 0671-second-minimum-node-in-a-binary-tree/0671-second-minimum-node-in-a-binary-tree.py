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

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        # Initialize variables for the final answer and the root value.

        # The root value is the minimum value by definition of the problem.

        self.second_minimum = -1

        self.root_value = root.val

      

        # Define a Depth-First Search (DFS) recursive function.

        def dfs(node):

            if node:

                # Recurse left sub-tree.

                dfs(node.left)

                # Recurse right sub-tree.

                dfs(node.right)

                # If the current node's value is greater than the root's value, 

                # it's a candidate for the second minimum.

                if node.val > self.root_value:

                    # If the second minimum hasn't been found yet, use this value,

                    # else update it only if we find a smaller value.

                    self.second_minimum = min(self.second_minimum, node.val) if self.second_minimum != -1 else node.val


        # Perform DFS starting from the root.

        dfs(root)

      

        # Return the second minimum value found; -1 if it doesn't exist.

        return self.second_minimum