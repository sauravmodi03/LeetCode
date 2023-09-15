class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

# nums = [0,1,2,2,3,0,4,2]
nums = [3,2,2,3]
val = 3

obj = Solution()
obj.removeElement(nums, val)