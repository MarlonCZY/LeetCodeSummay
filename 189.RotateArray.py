# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Reverse Array
        numsLen = len(nums)
        k = k % numsLen
        
        def reverseArray(arr, start, end):
            while(start < end):
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                
                start = start + 1
                end = end - 1
        
        if numsLen < 2:
            return 
        reverseArray(nums, 0, numsLen-1)
        reverseArray(nums, 0, k-1)
        reverseArray(nums, k, numsLen-1 )