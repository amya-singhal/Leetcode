class Solution:
    def count_pairs(self, dist: int, sortedNums: List[int]) -> int:
        left, count = 0, 0
        for right in range(1,len(sortedNums)):
            while sortedNums[right]-sortedNums[left] > dist:
                left += 1
            count += right-left
        return count
        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        left, right = 0, sortedNums[-1]-sortedNums[0]
        
        while left < right:
            mid = (right+left)//2
            pairs = self.count_pairs(mid, sortedNums)
            if pairs >= k:
                right = mid
            else:
                left = mid+1
        return left