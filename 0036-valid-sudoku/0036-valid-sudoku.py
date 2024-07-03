class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == ".":
                    continue
                else:
                    if num in r[row] or num in c[column] or num in boxes[(row // 3, column // 3)]:
                        return False
                    r[row].add(num)
                    c[column].add(num)
                    boxes[(row // 3, column // 3)].add(num)
        return True
                    
        