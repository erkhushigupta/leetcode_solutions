# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # Helper function to calculate the sum of all nodes' values in the tree

        def calculate_tree_sum(node: Optional[TreeNode]) -> int:

            if node is None:

                return 0

            # Sum the node's value and the sum of left and right subtrees

            return node.val + calculate_tree_sum(node.left) + calculate_tree_sum(node.right)


        # Helper function to find the maximum product of splitting the tree

        def find_max_product(node: Optional[TreeNode]) -> int:

            if node is None:

                return 0

          

            # Calculate the sum of the current subtree

            current_sum = node.val + find_max_product(node.left) + find_max_product(node.right)

          

            # Check if we can maximize the product using the sum of the current subtree

            if current_sum < total_sum:

                nonlocal max_product  # Allows us to modify the outer scope's max_product variable

                max_product = max(max_product, current_sum * (total_sum - current_sum))

          

            return current_sum


        modulo_base = 10**9 + 7

        total_sum = calculate_tree_sum(root)  # Getting the sum of all nodes in the tree

        max_product = 0

        find_max_product(root)  # Running the DFS function to find the maximum product

      

        return max_product % modulo_base   # Return the result modulo 10**9 + 7