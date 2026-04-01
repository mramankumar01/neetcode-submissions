class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p = 0
        for q in range(1, len(nums)):
            if nums[p] == nums[q]:
                return True
            p = q
        return False