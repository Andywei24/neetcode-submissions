class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWs = len(grid)
        COLs = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        def dfs(r, c):
            if r >= ROWs or c >= COLs or r < 0 or c < 0 or grid[r][c] == "0":
                return
            # visited
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for r in range(ROWs):
            for c in range(COLs):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands