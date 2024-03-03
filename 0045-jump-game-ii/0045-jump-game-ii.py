class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        nums = [2,3,1,1,4]
        dp = [2,1,2,1,0]
        4
        jump = 0
        q = [0]
        q = [1,2]
        q = [3,4]
        """
        jump = 0
        q = [0]
        visit = set()
        while q: # [0], [1,2], [3,4], 
            for _ in range(len(q)):
                x = q.pop(0) #0, 1, 2, 3, 4
                if x == len(nums)-1:
                    return jump
                for i in range(1,nums[x]+1): # 1,2
                    if i+x < len(nums) and (i+x) not in visit:
                        q.append(i+x)
                        visit.add(i+x)
            jump += 1