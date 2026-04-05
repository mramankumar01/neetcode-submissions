class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            tmp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                tmp *= nums[j]
            output.append(tmp)

        return output