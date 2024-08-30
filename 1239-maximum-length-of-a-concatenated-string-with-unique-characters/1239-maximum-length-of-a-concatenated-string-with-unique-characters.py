class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def check_unique(s: str) -> bool:
            unique = set()
            for char in s:
                if char in unique:
                    return False
                unique.add(char)
            return True
        
        
        final_ans = 0
        def get_substrings(index, tmp):
            nonlocal final_ans
            if check_unique(tmp):
                final_ans = max(final_ans, len(tmp))
            if index == len(arr):
                return
            get_substrings(index+1, tmp+arr[index])
            get_substrings(index+1, tmp)
            return
        
        get_substrings(0, "")
        return final_ans        