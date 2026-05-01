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
        sizes = []
        res = []
        i = 0

        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1

        i += 1
        for sz in sizes:
            res.append(s[i : i + sz])
            i = i + sz

        return res