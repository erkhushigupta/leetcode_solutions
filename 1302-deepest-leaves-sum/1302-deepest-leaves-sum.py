# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, ans, qlen, curr = [root], 0, 0, 0
        while len(q):
            qlen, ans = len(q), 0
            for _ in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return ans

        