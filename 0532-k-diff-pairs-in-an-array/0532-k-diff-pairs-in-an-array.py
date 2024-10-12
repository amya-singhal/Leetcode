class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        if k == 0:
            for key in count.keys():
                if count[key] > 1:
                    ans += 1
        else:
            for key in count.keys():
                if key+k in count:
                    ans += 1
            
        return ans