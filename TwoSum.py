# Solution to Two Sum https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for i, num1 in enumerate(nums):
            diff = target - num1
            if diff in values.keys():
                return [values[diff], i]
            else:
                values[num1] = i
        else:
            return None


if __name__ == "__main__":

    a = [1, 2, 5, 8, 20, 9, 6]
    sol = Solution()

    # Returns index 2, 5
    # a[2] + a[5] = 14
    print(sol.twoSum(a, 14))
