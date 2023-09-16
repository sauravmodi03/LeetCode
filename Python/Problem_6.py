class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        d = k
        if (len(nums) <= 1):
            return
        if d > n:
            d = d % n
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, d - 1)
        reverse(nums, d, len(nums) - 1)


def reverse(nums, l, h):
    low = l
    high = h
    while low < high:
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp
        low += 1
        high -= 1


nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
obj.rotate(nums, k)