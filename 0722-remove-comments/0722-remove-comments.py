class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # // we just ignore the rest of the line and move to next source[i]
        # if we get /*, we check for */ in i and other i+n sources till we find         # it
        # for loop on source i = 0 to length of source
        # example 1
        # for every new source we can keep empty and after we find comment we can chack if tmp is not empty, we add that part of the string before the comment
        # blockComment = False
        # i = 0, we find /* but we also find */, so nothing left to search just         # do i++
        # i = 1found no comments and not blank so move ahead, ADD TO ANS
        # i = 2 same as 1, ADD TO ANS
        # i = 3, found // so skip if tmp is empty
        # i = 4 same as 1, ADD TO ANS
        # i = 5, find /* but not */, set blockComment = True, skipped
        # i = 6, */ not found, skip
        # i = 7, */ not found, skip
        # i = 8 found, skip this too, set blockComment = False
        # i = 9 same as 1, ADD TO ANS
        # i = 10 same as 1, ADD TO ANS
        
        ans = []
        modified = ""
        commenting = False
        # main for loop
        for line in source:
            # print(line)
            i = 0
            # inside every line
            while (i < len(line)):
                if i+1 == len(line):
                    if not commenting:
                        modified += line[i]
                    i += 1
                    break
                twoChar = line[i:i+2]
                if twoChar == "//":
                    if not commenting:
                        break
                    else:
                        i += 2
                elif twoChar == "/*" and not commenting:
                    commenting = True
                    i += 2
                elif twoChar == "*/" and commenting:
                    commenting = False
                    i += 2
                else:
                    if not commenting:
                        modified += line[i]
                        # print(line, i, modified)
                    i += 1
            if modified and not commenting:
                ans.append(modified)
                modified = ""
        return ans
            