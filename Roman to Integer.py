    def romanToInt(self,s:str)->int:
        convertedInt = 0
        romanHashmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        prevChar = None
        for i in range(0,len(s)):
            currChar=s[i]
            if (i>0) and (romanHashmap[
            currChar]>romanHashmap[prevChar]):
                convertedInt = convertedInt - 2*romanHashmap[prevChar] + romanHashmap[currChar]
            else:
                    convertedInt += romanHashmap[currChar]
            prevChar=currChar
        return convertedInt
