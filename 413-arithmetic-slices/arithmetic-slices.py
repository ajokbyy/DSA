class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        count = 0      # total arithmetic slices
        curr = 0       # slices ending at current index

        for i in range(2, n):
            # check if last 3 numbers form arithmetic sequence
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1        # extend previous slices
                count += curr   # add to total
            else:
                curr = 0        # reset if not arithmetic

        return count
