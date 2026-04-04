class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res =[]
        for li in matrix:
            res.extend(li)

        l, r = 0, len(res) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if res[mid] == target:
                return True
            elif res[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False