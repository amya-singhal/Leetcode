class Solution:
    def numTrees(self, n: int) -> int:
        if (n == 0 or n == 1):
            return 1
        array = []
        array.append(1)
        array.append(1)
        for j in range(2, n+1):
            count = 0
            for i in range(1, j+1):
                count += array[i-1]* array[j-i]
            array.append(count)
        return array[n]