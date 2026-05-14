class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWs, COLs = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWs or nc >= COLs or grid[nr][nc] == "0":
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
                 
                    
            
        for r in range(ROWs):
            for c in range(COLs):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        return islands