class Solution(object):
    def maxArea(self, height):
        area = 0
        mn = 0
        mx = len(height)-1
        a = 0
        while mn < mx:
            if height[mn] < height[mx]:
                a = height[mn] * (mx - mn)
                mn += 1
            else:
                a = height[mx] * (mx - mn)
                mx -= 1
            area = max(area, a)
        print(area)

height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
obj.maxArea(height)