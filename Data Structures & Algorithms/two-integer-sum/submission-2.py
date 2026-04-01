class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append([num, i])

        arr.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = arr[l][0] + arr[r][0]
            if curr_sum == target:
                return [min(arr[l][1], arr[r][1]),
                        max(arr[l][1], arr[r][1])]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
        return
