class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


nums = [2,2,1,1,1,2,2]

obj = Solution()
obj.majorityElement(nums)