class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def sum_consecutive_pairs(self):
        temp = self.head
        result = []
        while temp and temp.next:
            pair_sum = temp.data + temp.next.data
            result.append(pair_sum)
            temp = temp.next  # move to next node
        return result

# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Sum of consecutive pairs:", ll.sum_consecutive_pairs())
