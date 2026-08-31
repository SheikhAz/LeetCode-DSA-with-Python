# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        def dfs(root):
            if not root:
                return [0,0]
            leftpair = dfs(root.left)
            rightpair = dfs(root.right)
            withRoot = root.val + leftpair[1] + rightpair[1]
            withoutRoot = max(leftpair) + max(rightpair)
            return [withRoot, withoutRoot]
        return max(dfs(root))
        