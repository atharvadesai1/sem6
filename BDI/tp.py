class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
        if not head:
            return head
        if not head.next:
            return head
        nums = []
        current_node = head
        while current_node:
            nums.append(current_node.val)
            current_node = current_node.next
        print(nums)
        nums.reverse()
        print(nums)

        top = ListNode()
        top.val = nums[0]
        top.next = ListNode()
        current_node = top.next
        for i in range(1,len(nums)):
            current_node.val = nums[i]
            if i != len(nums)-1:
                current_node.next = ListNode()
                current_node = current_node.next
        return top

l = [1,2,3,4,5]
head = ListNode()
head.val = l[0]
head.next = ListNode()
current_node = head.next
for i in range(1,len(l)):
     current_node.val = l[i]

current_node.next = ListNode()
current_node = current_node.next
current_node.val = 3

ans = reverseList(head)
print(f'Ans: {ans.val} ==> {ans.next.val} ==> {ans.next.next.val}')