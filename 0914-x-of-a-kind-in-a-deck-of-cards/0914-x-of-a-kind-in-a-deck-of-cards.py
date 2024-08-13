class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def find_gcd(x, y):
            while(y):
                x, y = y, x % y

            return x
        
        count = Counter(deck)
        if len(count) == 1:
            return min(count.values()) > 1
        l = list(count.values())
        gcd=find_gcd(l[0],l[1])
        
        for i in range(2,len(l)):
            gcd=find_gcd(gcd,l[i])
        return gcd != 1