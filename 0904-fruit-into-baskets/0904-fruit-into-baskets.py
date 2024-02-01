class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        [1,2,3,2,2]
        c= {2:3, 3:1}
        ans = 1, 2, 2, 3, 4
        j = 0, 1
        """
        c = defaultdict(int)
        j = 0
        ans = 0
        for i in range(len(fruits)):
            #print(c)
            c[fruits[i]] += 1
            while(len(c) > 2):
                c[fruits[j]] -= 1
                if c[fruits[j]] == 0:
                    del c[fruits[j]]
                j += 1
            ans = max(ans, i-j+1)
        return ans
    
                