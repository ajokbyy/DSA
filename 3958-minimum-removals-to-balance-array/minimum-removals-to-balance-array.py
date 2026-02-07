class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        j = 0
        max_len = 1
        
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            
            max_len = max(max_len, j - i)
        
        return n - max_len
        