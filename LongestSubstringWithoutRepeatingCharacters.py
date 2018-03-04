# Solution to https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [i for i in s]

        max_length = 0
        length = 0
        items = []

        for i in chars:
            if i not in items:
                items.append(i)
                length += 1
            else:
                # Check if greater than max length
                max_length = max(max_length, length)

                # Get index of previous occurrence
                ind = items.index(i)

                # Create new sub-list
                items = items[(ind + 1):]

                # Append new item
                items.append(i)

                length = len(items)

        return max(length, max_length)


if __name__ == "__main__":

    sol = Solution()
    print(sol.lengthOfLongestSubstring("Testing this string"))
