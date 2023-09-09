class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2 # 11
        subset = set()
        subset.add(0) # (1), (1,5,6), (11, 17, 15, 12)
        for n in nums:
            # print(subset)
            tmp = set()
            for s in subset:
                tmp.add(s)
                tmp.add(s+n)
            subset = tmp
            if target in subset:
                return True
        return False
                
        
        
        