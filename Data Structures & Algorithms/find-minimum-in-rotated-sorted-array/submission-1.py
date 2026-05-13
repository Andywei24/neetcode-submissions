class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for i, num in enumerate(nums):
            if num < smallest:
                smallest = num

              
        return smallest