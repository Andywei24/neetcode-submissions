class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        hashMap = {i:[] for i in range(n)}
        for node, child in edges: 
            hashMap[node].append(child)
            hashMap[child].append(node)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in hashMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True


        return dfs(0, -1) and len(visited) == n
