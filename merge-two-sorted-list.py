def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    result_node = []
    l1_cur_val = l1.value
    l2_cur_val = l2.value
    next_val = l1.next
    print(next_val)

    if l1_cur_val < l2_cur_val:
        result_node.append(l1_cur_val)
        l1_cur_val = l1.next
    else: 
        result_node.append(l2_cur_val)
        l2_cur_val = l2.next          

    print(result_node)

mergeTwoLists([1,2,4],[2,3,6])