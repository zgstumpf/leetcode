# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # rename argument so it makes sense after we leave root
        node = root
        
        # if node is None, do nothing
        if node:
            # swap
            node.left, node.right = node.right, node.left

            # recursively call invert on node's children
            self.invertTree(node.left)
            self.invertTree(node.right)
        
        return root
