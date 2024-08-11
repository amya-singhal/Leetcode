class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def checkSorted(arr):
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    return False
            return True
        
        for i in range(1, len(nums)-1):
            newA = nums[0:i]+ nums[i+1:]                
            if nums[i-1] < nums[i+1] and (nums[i]<= nums[i-1] or nums[i] >= nums[i+1]):
                return checkSorted(newA)
            
        return checkSorted(nums[1:]) or checkSorted(nums[:-1])