class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution 1:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = True

        return False
            