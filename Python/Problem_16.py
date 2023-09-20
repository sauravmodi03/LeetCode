class Solution:
    def productExceptSelf(self, nums):
        l = 1
        r = len(nums) - 2
        res = [1] * len(nums)

        left = 1
        right = 1
        while l < len(nums) and r >= 0:
            left *= nums[l - 1]
            right *= nums[r + 1]

            res[l] = res[l] * left
            res[r] = res[r] * right

            l += 1
            r -= 1

        return res

nums = [1,2,3,4]
obj = Solution()
obj.productExceptSelf(nums)