class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1,2,5], amount = 11
        q = [(0,0)]
        q = [(1,1),(2,1),(5,1)]
        q = [(5,1),(3,2),(6,2),(4,2),(7,2)]
        """
        q = deque()
        q.append((0,0))
        visit = set()
        while q:
            cur_coin, count = q.popleft()
            if cur_coin == amount:
                return count
            
            for coin in coins:
                next_coin = cur_coin+coin
                if next_coin <= amount and next_coin not in visit:
                    visit.add(next_coin)
                    q.append((next_coin, count+1))
        return -1