class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for n, c in counter.items():
            heapq.heappush(heap, (c, n))

        return [n for c, n in heapq.nlargest(k, heap)]