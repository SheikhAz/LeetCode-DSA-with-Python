class Solution(object):
    def letterCombinations(self, digits):
        hashMap = {
                        "2":'abc',
                        "3":"def",
                        "4":'ghi',
                        "5":'jkl',
                        "6":'mno',
                        "7":'pqrs',
                        "8":'tuv',
                        "9":'wxyz'
                    }
        result = []
        def backtrack(i,curStr):
            if len(digits) == len(curStr):
                result.append(curStr)
                return
            for c in hashMap[digits[i]]:
                backtrack(i+1,curStr + c)
        if digits:
            backtrack(0,'')
        return result

        