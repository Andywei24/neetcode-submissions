class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                if (j - i + 1) - max(count.values()) <= k:
                    res = max(res, j - i + 1)
        return res