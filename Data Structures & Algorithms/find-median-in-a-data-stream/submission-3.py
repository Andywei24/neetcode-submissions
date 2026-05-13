class MedianFinder:

    def __init__(self):
        self.lo = [] # Max heap
        self.hi = [] # Min heap

    def addNum(self, num: int) -> None:
        # Add num to lo
        heapq.heappush(self.lo, -num)

        # Rebalance upwards
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        # Reblance backwards if hi > lo
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.hi) == len(self.lo):
            return (self.hi[0] + (-self.lo[0])) / 2
        
        else:
            return -self.lo[0]