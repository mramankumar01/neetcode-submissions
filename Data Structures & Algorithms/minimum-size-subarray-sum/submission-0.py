class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        res = float('inf')
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:   # window is valid - try to shrink
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
        return res if res != float('inf') else 0
