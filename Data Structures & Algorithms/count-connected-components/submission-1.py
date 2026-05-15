class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap = {i:[] for i in range(n)}
        for node, child in edges:
            hashMap[node].append(child)
            hashMap[child].append(node)
        visit = [False] * n
        def dfs(node):
            for nei in hashMap[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
