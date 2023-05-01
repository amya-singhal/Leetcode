class Solution(object):
    def average(self, salary):
        salary.sort()
        length = len(salary)
        sum = 0
        for i in range (1, length - 1):
            sum += salary[i]
        return float(sum) / float((length - 2))
        """
        :type salary: List[int]
        :rtype: float
        """