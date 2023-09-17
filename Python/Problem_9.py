class Solution(object):
    def romanToInt(self, s):
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = ""
        for x in s:
            if ((prev == "I" and x in ("V", "X")) or
                    (prev == "X" and x in ("L", "C")) or
                    (prev == "C" and x in ("D", "M"))):
                total = total + dict[x] - dict[prev]
                prev = ""
            else:
                if prev == "":
                    prev = x
                else:
                    total += dict[prev]
                    prev = x
        if prev != "":
            total += dict[prev]
        return total

s = "MCMXCIV"
obj = Solution()
obj.romanToInt(s)