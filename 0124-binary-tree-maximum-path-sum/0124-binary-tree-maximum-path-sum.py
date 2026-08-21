class Solution(object):
    def maxPathSum(self, root):
        maxi = [float('-inf')]
        def dfs(node):
            if node is None:
                return 0
            leftsum = dfs(node.left)
            leftsum = max(0, leftsum)
            rightsum = dfs(node.right)
            rightsum = max(0, rightsum)
            current = leftsum + node.val + rightsum
            maxi[0] = max(maxi[0], current)
            return node.val + max(leftsum, rightsum)
        dfs(root)
        return maxi[0]
        