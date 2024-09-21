class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        double = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        places = ["Hundred", "Thousand", "Million"]
        
        billions, num = divmod(num, 1000000000)
        millions, num = divmod(num, 1000000)
        thousands, num = divmod(num,1000)
        
        def to_words(subN):
            ans = []
            if len(str(subN)) == 3:
                d, twoDigit = divmod(subN, 100)
                ans += [digits[d], 'Hundred']
                subN = twoDigit
            if subN < 20:
                ans.append(digits[subN])
            else:
                d, singleD = divmod(subN, 10)
                ans += [double[d], digits[singleD]]
            return ans
        
        # print(billions,millions,thousands,num)
        finalList = []
        if billions:
            finalList += to_words(billions) + ["Billion"]
        if millions:
            finalList += to_words(millions) + ["Million"]
        if thousands:
            finalList += to_words(thousands) + ["Thousand"]
        if num:
            finalList += to_words(num)
        finalList = [word for word in finalList if word]
        # print(finalList)
        if len(finalList) == 1:
            return finalList[0]
        return " ".join(finalList)
            
        