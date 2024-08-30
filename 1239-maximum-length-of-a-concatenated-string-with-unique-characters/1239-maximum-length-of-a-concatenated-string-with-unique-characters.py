class Solution:
    def maxLength(self, arr: List[str]) -> int:
        final_ans = 0
        def get_substrings(index, tmp):
            nonlocal final_ans
            if index == len(arr):
                if len(tmp) == len(set(tmp)):
                    final_ans = max(final_ans, len(tmp))
                return
            get_substrings(index+1, tmp+arr[index])
            get_substrings(index+1, tmp)
            return
        
        get_substrings(0, "")
        return final_ans        