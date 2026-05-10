# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        count = [k]
        def inorder(node):
            if not node or count[0] == 0: return
            inorder(node.left)
            count[0] -= 1
            if count[0] == 0:
                res[0] = node.val
                return
            inorder(node.right)
        inorder(root)
        return res[0]