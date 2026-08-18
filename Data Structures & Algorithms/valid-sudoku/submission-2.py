class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])


        for box in range(9):
            seen = set()
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    val = board[start_row + i][start_col + j]
                    if val != '.':
                        if val in seen:
                            return False
                        seen.add(val)

        return True

        
