class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)- 1

        max_jump_index, min_jumps, max_jump_limit = 0, 0, 0

        for i in range(n):
            max_jump_index= max(max_jump_index, i+ nums[i])

            if i== max_jump_limit:
                print(max_jump_limit)
                min_jumps+= 1
                max_jump_limit= max_jump_index

        return min_jumps