class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        "2", "3"
        ["0","1","2","3","4","5","6","7","8","9"]
        x = 1
        int1 = 3*x = 3
        x = 10
        int1 = int1 + 2*x = 23
        x = 100
        int1 = int1 + 1*x = 123
        int2 = 456
        sum1 = 56088
        """
        d = {"0": 0, "1": 1, "2" : 2, "3": 3, "4": 4, "5": 5, "6":6, "7":7, "8":8, "9": 9}
        int1 = 0
        x = 1
        for i in reversed(num1):
            int1 = int1 + d[i]*x
            x = x*10
        int2 = 0
        y = 1
        for i in reversed(num2):
            int2 = int2 + d[i]*y
            y = y*10
        prod = int1*int2
        return str(prod)
            
        
        
        