class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        if i < len(left):
            result.extend(left[i:])
        if j < len(right):
            result.extend(right[j:])
        return result