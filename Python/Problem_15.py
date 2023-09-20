class Solution(object):
    def jump(self, nums):
        n = 0
        jump = 0
        i = 0
        while i < len(nums) - 1 and nums[i] != 0:
            n = max(n, i + nums[i])
            i = i + nums[i]
            jump += 1
            if n >= len(nums) - 1:
                print(n, jump)
                return jump
        print(0)

nums = [1,2,1,1,1]
obj = Solution()

obj.jump(nums)