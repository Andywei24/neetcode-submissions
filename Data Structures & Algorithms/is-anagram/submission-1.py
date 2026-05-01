class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: Sorting
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # Solution 2: Hash table
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26

        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False
        
        # return True

        # Solution 3: 2 Hash map
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT



