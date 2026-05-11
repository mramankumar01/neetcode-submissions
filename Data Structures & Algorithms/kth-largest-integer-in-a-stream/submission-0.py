class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k    = k           # store k
        self.heap = nums        # start with given numbers

        heapq.heapify(self.heap)         # make it a valid min-heap O(n)

        while len(self.heap) > k:        # trim to only k elements
            heapq.heappop(self.heap)     # remove smallest repeatedly

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)   # add new value

        if len(self.heap) > self.k:      # if heap exceeds k
            heapq.heappop(self.heap)     # remove smallest

        return self.heap[0]              # root = kth largest