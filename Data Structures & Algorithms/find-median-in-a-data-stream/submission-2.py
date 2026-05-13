class MedianFinder:

    def __init__(self):
        self.lower_max_heap = []
        self.upper_min_heap = []


    def addNum(self, num: int) -> None:
        # print("----Add num start-----")
        # print("lower =", self.lower_max_heap)
        # print("upper =", self.upper_min_heap)

        # Step 1: insert into the appropriate heap
        if not self.lower_max_heap or num <= -self.lower_max_heap[0]:
            heapq.heappush(self.lower_max_heap, -num)
        else:
            heapq.heappush(self.upper_min_heap, num)

        # Step 2: rebalance sizes
        if len(self.lower_max_heap) > len(self.upper_min_heap) + 1:
            val = -heapq.heappop(self.lower_max_heap)
            heapq.heappush(self.upper_min_heap, val)

        elif len(self.upper_min_heap) > len(self.lower_max_heap) + 1:
            val = heapq.heappop(self.upper_min_heap)
            heapq.heappush(self.lower_max_heap, -val)

        # print("lower =", self.lower_max_heap)
        # print("upper =", self.upper_min_heap)

    def findMedian(self) -> float:
        # print("----Find median start-----")
        lower_max_heap = self.lower_max_heap
        upper_min_heap = self.upper_min_heap
        
        if (len(lower_max_heap) + len(upper_min_heap)) % 2 == 0:
            val1 = -lower_max_heap[0] 
            val2 = upper_min_heap[0]
            return ( val1 + val2 ) / 2
        else:
            # print("lower =", lower_max_heap)
            # print("upper =", upper_min_heap )

            if len(lower_max_heap) > len(upper_min_heap):
                return -lower_max_heap[0]
            else:
                return upper_min_heap[0]