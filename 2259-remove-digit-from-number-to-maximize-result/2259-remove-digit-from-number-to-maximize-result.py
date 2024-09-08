class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = 0
        """
        number = "1231", digit = "1"
        """
        for i in range(len(number)):
            if number[i] == digit:
                tmp_num = number[:i]+number[i+1:]
                max_result = max(max_result, int(tmp_num))
        
        return str(max_result)
            