class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROWs, COLs = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWs or c >= COLs or board[r][c] != "O":
                return 
            # visited.add((r,c))
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWs):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLs - 1] == "O":
                dfs(r, COLs - 1)

        for c in range(COLs):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWs - 1][c] == "O":
                dfs(ROWs - 1, c)
        
        for r in range(ROWs):
            for c in range(COLs):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"