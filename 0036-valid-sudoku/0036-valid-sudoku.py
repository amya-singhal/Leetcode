class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        box = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                else:
                    if num in r[row] or num in c[col] or num in box[(row // 3, col // 3)]:
                        return False
                    r[row].add(num)
                    c[col].add(num)
                    box[(row // 3, col // 3)].add(num)
        return True