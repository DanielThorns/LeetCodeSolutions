# Solution to https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type c: int
        :rtype: ListNode
        """

        n = ListNode(0)
        total = l1.val + l2.val + c
        carry = int(math.floor(total / 10))

        n.val = total - carry * 10

        if l1.next is None and l2.next is None:
            if carry > 0:
                n.next = ListNode(carry)
            return n
        elif l1.next is None:
            l1.next = ListNode(0)
        elif l2.next is None:
            l2.next = ListNode(0)

        n.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return n


if __name__ == "__main__":
    import math

    # Example: 243 + 564 = 807

    # Create 243 reverse linked list
    l11 = ListNode(2)
    l12 = ListNode(4); l12.next = l11
    l13 = ListNode(3); l13.next = l12

    # Create 564 reverse linked list
    l21 = ListNode(5)
    l22 = ListNode(6); l22.next = l21
    l23 = ListNode(4); l23.next = l22

    # Return solution as reverse linked list
    sol = Solution()
    v = sol.addTwoNumbers(l13, l23)

    # Print solution
    ans = list()
    while v is not None:
        ans.append(v.val)
        v = v.next
    print(ans[::-1])
