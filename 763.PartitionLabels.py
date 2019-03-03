# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        d = {c:i for c, i in enumerate(S)}
        j = anchor = 0
        
        for i in range(len(S)):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        