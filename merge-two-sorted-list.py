class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = ListNode(1)
        trail = result_list
        while (l1 and l2):
            if l1.val <= l2.val:
                trail.next = l1
                l1 = l1.next
                trail = trail.next
            else: 
                trail.next = l2
                l2 = l2.next
                trail = trail.next
        if l1:
            trail.next = l1
        elif l2:
            trail.next = l2
        return result_list.next
    



