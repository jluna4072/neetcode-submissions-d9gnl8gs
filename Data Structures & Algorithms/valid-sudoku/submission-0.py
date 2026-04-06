class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        cols_dict= defaultdict(set)
        rows_dict= defaultdict(set)
        sqr_dict = defaultdict(set)
        
        for i in range(ROWS):
            for j in range(COLS):
                n = board[i][j]
                if n == ".":
                    continue
                if (n in cols_dict[j] or
                    n in rows_dict[i] or
                    n in sqr_dict[(i // 3, j // 3)]):
                    return False
                cols_dict[j].add(n)
                rows_dict[i].add(n)
                sqr_dict[(i // 3, j // 3)].add(n)
        
        return True
