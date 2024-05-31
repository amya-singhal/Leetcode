class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        l = len(nums)
        def helper(index, tmp):
            nonlocal nums, l
            if index == l:
                return
            tmp.append(nums[index])
            ans.append(tmp.copy())
            helper(index+1, tmp.copy())
            tmp.pop()
            helper(index+1, tmp)
        helper(0, [])
        return ans
            
        