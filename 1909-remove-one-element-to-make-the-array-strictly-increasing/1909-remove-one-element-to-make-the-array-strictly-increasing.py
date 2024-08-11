class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def checkSorted(arr):
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    return False
            return True
        
        for i in range(len(nums)):
            newA = nums[0:i]+ nums[i+1:]
            if checkSorted(newA):
                return True
            
        return False