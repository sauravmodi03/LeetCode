class Solution(object):
    def reverseWords(self, s):
        strs = s.split()
        low = 0
        high = len(strs) - 1
        while low < high:
            temp = strs[low]
            strs[low] = strs[high]
            strs[high] = temp
            low += 1
            high -= 1
        print(" ".join(strs))
        return " ".join(strs)

obj = Solution()
obj.reverseWords("sky is blue ")