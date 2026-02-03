class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        
        # A trionic array must have at least 3 segments
        # So total length must be at least 4
        # (increase → decrease → increase, each needs comparison)
        if n < 4:
            return False
        
        i = 0
        
        # -----------------------------
        # First segment: strictly increasing
        # Move forward while nums[i] < nums[i+1]
        # This finds the peak p
        # -----------------------------
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        # p cannot be at index 0
        # because first segment must have at least 2 elements
        if i == 0:
            return False
        
        # -----------------------------
        #  Second segment: strictly decreasing
        # Move forward while nums[i] > nums[i+1]
        # This finds the valley q
        # -----------------------------
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        
        # If no decreasing happened,
        # then the second segment does not exist
        if i == n - 1:
            return False
        
        # -----------------------------
        #  Third segment: strictly increasing
        # Move forward while nums[i] < nums[i+1]
        # This must reach the last index
        # -----------------------------
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        # If we successfully reached the end,
        # then all three segments exist and are valid
        return i == n - 1
