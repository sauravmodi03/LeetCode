class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        for i in range(0, n):
            nums1[i+m] = nums2[i];
        print(nums1)
        for i in range(m+n):
            for j in range (m+n):
                if nums1[i] < nums1[j]:
                    min = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = min


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
obj = Solution()
obj.merge(nums1, 3, nums2, 3)