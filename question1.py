class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}

        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3

    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
    