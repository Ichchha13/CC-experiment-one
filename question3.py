class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)
        mid = n // 2

        if n % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]

    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
