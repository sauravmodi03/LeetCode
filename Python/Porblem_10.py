class Solution(object):
    def intToRoman(self, num):
        dict = {1000: "M", 900:"CM", 500: "D", 400:"CD", 100: "C", 90:"XC", 50: "L", 40:"XL", 10: "X", 9:"IX", 5: "V", 4:"IV", 1: "I"}
        n = num
        res = ""
        for key, value in reversed(sorted(dict.items())):
            ln = len(str(n))-1
            d = 10 ** ln
            k = (n // d) * d
            if key == k:
                res += value
                n = n%d
            elif k > key:
                res += value + (((k-key)//d) * dict[d])
                n = n%d
        return res

obj = Solution()
obj.intToRoman(58)