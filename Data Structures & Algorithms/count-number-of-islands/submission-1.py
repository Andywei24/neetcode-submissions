class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWs, COLs = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWs or c >= COLs or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for r in range(ROWs):
            for c in range(COLs):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands