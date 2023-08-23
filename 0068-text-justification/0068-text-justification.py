class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tmp = []
        l = 0
        justifiedText = []
        for w in words:
            if l + len(w) + len(tmp) > maxWidth:
                spaces = maxWidth - l
                for i in range(maxWidth - l):
                    tmp[i%(len(tmp) - 1 or 1)] += ' '
                justifiedText.append(''.join(tmp))
                tmp = []
                l = 0
            l += len(w)
            tmp.append(w)
        return justifiedText + [' '.join(tmp).ljust(maxWidth)]
                
        