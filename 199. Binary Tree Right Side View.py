# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.sideDict = dict()
        self.dfs(root, 0)
        return list(self.sideDict.values())
    def dfs(self, root, depth):
        if not root:
            return 
        if depth not in self.sideDict:
            self.sideDict[depth] = root.val
        self.dfs(root.right, depth+1)
        self.dfs(root.left, depth+1)