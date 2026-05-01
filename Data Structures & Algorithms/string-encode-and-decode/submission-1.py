class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        res = ""

        for string in strs:
            sizes.append(len(string))
        
        for size in sizes:
            res += str(size)
            res += ','
        res += '#'

        for string in strs:
            res += string
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        sizes =[]
        res = []
        
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        
        i += 1
        for size in sizes:
            res.append(s[i : i + size])
            i = i + size
        return res

        