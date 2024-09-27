class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        sums = 0
        ans = 0
        # 1 2
        for num in nums:
            sums += num
            if sums - k in d:
                ans += d[sums - k]
            d[sums] += 1
        
        return ans