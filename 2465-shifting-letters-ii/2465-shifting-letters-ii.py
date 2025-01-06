class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        f_shifts = [0]* (len(s)+1)
        for start, end, dire in shifts:
            if dire == 0:
                f_shifts[start] -= 1
                if end + 1 < len(s):
                    f_shifts[end+1] += 1
            else:
                f_shifts[start] += 1
                if end + 1 < len(s):
                    f_shifts[end+1] -= 1
        net_shift = 0
        result = []
        for i in range(len(s)):
            net_shift += f_shifts[i]
            new_char = chr((ord(s[i]) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)

        return "".join(result)