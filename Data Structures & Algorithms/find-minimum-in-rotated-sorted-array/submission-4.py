class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for num in nums:
            if num < smallest:
                smallest = num
        return smallest