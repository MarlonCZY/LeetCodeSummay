# Time Complexity: O(N)
# Spcae Complexity: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        
        return self.dfs(root)
        
    def dfs(self, root):
        if root.val > self.p.val and root.val > self.q.val:
            return self.dfs(root.left)
        elif root.val < self.p.val and root.val < self.q.val:
            return self.dfs(root.right)
        else:
            return root