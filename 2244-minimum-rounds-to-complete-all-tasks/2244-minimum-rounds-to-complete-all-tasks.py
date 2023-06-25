class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        v = []
        rounds = 0
        count = Counter(tasks)
        for c in count.values():
            if c < 2:
                return -1
            if c <= 3:
                rounds += 1
            else:
                rounds += c//3
                if c%3:
                    rounds += 1
        return rounds