class Solution(object):
    def lengthOfLastWord(self, s):
        data = s.split(" ")
        print(data)
        for i in range(len(data)-1,-1,-1):
            length = len(data[i])
            print(length)
            if length > 0:
                return length
        return 0

obj = Solution()
obj.lengthOfLastWord("a")