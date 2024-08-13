# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
class Solution:
  def postorderTraversal(self, root: TreeNode | None) -> list[int]:
    ans = []

    def postorder(root: TreeNode | None) -> None:
      if not root:
        return

      postorder(root.left)
      postorder(root.right)
      ans.append(root.val)

    postorder(root)
    return ans