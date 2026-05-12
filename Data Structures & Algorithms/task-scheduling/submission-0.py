class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    cooldown.append((time + n, cnt))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
        return time