class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        YYNY
        index 0: (1, index+1, closed), (0, index+1, open)
        index 1: (2, index+1, closed), (1, index+1, closed), (0, index+1, open)
        index 2: (2, index+1, closed), (1, index+1, closed), (1, index+1, closed), (1, index+1, closed)
        
        """
        max_points = 0
        hour = -1
        points = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                points += 1
            else:
                points -= 1
            if points > max_points:
                hour = i
                max_points = points
            
        return hour+1
                