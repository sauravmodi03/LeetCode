class Solution(object):
    def removeDuplicates(self, nums):
        prev = nums[0]
        count = 1
        i = 0
        for j in range(1,len(nums)):
            if prev == nums[j] and count < 2:
                count +=1
                i += 1
                if nums[i] != prev or j == len(nums)-1:
                    nums[i] = prev
            elif prev < nums[j] and i < j:
                i += 1
                nums[i] = nums[j]
                prev = nums[j]
                count = 1
        return i+1

nums = [1,1,1,1,2,2,3]

obj = Solution()
obj.removeDuplicates(nums)