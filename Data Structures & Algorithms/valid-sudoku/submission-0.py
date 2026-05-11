class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        boxes=defaultdict(set)
        for row in range(9):
            for col in range(9):
                box=(row//3,col//3)
                if board[row][col]==".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[box]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[box].add(board[row][col])
        return True

        