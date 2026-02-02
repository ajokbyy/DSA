class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        wind_sum = 0
        for i in range(k):
            wind_sum += nums[i]

        max_sum = wind_sum

        for i in range(k, len(nums)):
            wind_sum += nums[i]
            wind_sum -= nums[i - k]

            max_sum = max(max_sum, wind_sum)
        return max_sum/k      