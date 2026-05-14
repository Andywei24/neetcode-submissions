class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWs = len(heights)
        COLs = len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r >= ROWs or c >= COLs or heights[r][c] < prevHeight or ((r, c) in visited):
                return 
            visited.add((r,c))
            prevHeight = heights[r][c]
            # dfs(r - 1, c, visited, prevHeight)
            # dfs(r + 1, c, visited, prevHeight)
            # dfs(r, c - 1, visited, prevHeight)
            # dfs(r, c + 1, visited, prevHeight)
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, prevHeight)

        for c in range(COLs):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWs - 1, c, atlantic, heights[ROWs - 1][c])
        
        for r in range(ROWs):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLs - 1, atlantic, heights[r][COLs - 1])
        
        res = []
        for r in range(ROWs):
            for c in range(COLs):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res