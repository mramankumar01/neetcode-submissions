class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0

        nums.sort()
        max_streak = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Skip duplicates
                if nums[i] == nums[i - 1] + 1:
                    curr_streak += 1
                else:
                    max_streak = max(max_streak, curr_streak)
                    curr_streak = 1
        return max(max_streak, curr_streak)
