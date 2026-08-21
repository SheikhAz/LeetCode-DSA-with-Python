class Solution(object):
    def dfs(self,root,sum,l,result):
        if not root.left and not root.right:
            if root.val == sum:
                result += [l + [root.val]]
        if root.right:
            self.dfs(root.right,sum - root.val,l+[root.val],result)
        if root.left:
            self.dfs(root.left,sum - root.val , l+[root.val],result)
        return result
    def pathSum(self, root, targetSum):
        if root is None:
            return []
        return self.dfs(root,targetSum,[],[])
        