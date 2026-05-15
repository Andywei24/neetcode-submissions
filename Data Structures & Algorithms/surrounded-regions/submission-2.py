class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWs, COLs = len(board), len(board[0])

        def bfs():
            queue = deque()
            for r in range(ROWs):
                for c in range(COLs):
                    if (r == 0 or r == ROWs - 1 or c == 0 or c == COLs - 1) and board[r][c] == "O":
                        queue.append((r,c))

            while queue:
                r, c = queue.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        if r+dr >= 0 and r+dr < ROWs and c+dc >= 0 and c+dc < COLs:
                            queue.append((r + dr, c + dc))
                    # for dr, dc in directions:
                    #     nr, nc = r + dr, c + dc
                    #     if 0 <= nr < ROWs and 0 <=nc < COLs:
                    #         queue.append((nr, nc))
        bfs()
        for r in range(ROWs):
            for c in range(COLs):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        