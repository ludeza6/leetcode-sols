# Last updated: 8/24/2026, 9:51:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def traverse(node):
            if not node:
                return
        
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return result