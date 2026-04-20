class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            cap = (l + r) // 2
            if self.canShip(weights, days, cap):
                res = cap
                r = cap - 1
            else:
                l = cap + 1
        return res

    def canShip(self, weights, days, cap):
        ships, curCap = 1, 0
        for w in weights:
            if curCap + w > cap:
                ships += 1
                curCap = 0
            curCap += w
        return ships <= days