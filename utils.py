def wasteTime(n):
    res=[]
    for i in range(n):
        res.append(i)
def printLinkedList(head):
    cur=head
    s=[]
    while cur:
        s.append(str(cur.val))
        s.append(' -> ')
        print(cur.val)
        wasteTime(100000)
        cur=cur.next
    print(''.join(s))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def buildTestLinkedList(n):
    head=ListNode(1)
    prevNode=head

    for i in range(2,n):
        curNode=ListNode(i)
        prevNode.next=curNode
        prevNode=curNode
    return head