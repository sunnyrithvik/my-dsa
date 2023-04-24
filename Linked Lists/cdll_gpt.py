class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the end of the list
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    # Insert a node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            first_node = self.head
            last_node = self.head.prev
            first_node.prev = new_node
            new_node.next = first_node
            new_node.prev = last_node
            last_node.next = new_node
            self.head = new_node

    # Delete a node by value
    def delete(self, key):
        if not self.head:
            return

        curr_node = self.head

        while curr_node.data != key:
            curr_node = curr_node.next
            if curr_node == self.head:
                return

        if curr_node.next == curr_node:  # Only one node
            self.head = None
            return

        next_node = curr_node.next
        prev_node = curr_node.prev

        if curr_node == self.head:
            self.head = next_node

        next_node.prev = prev_node
        prev_node.next = next_node

    # Print the list
    def print_list(self):
        if not self.head:
            return

        curr_node = self.head

        while True:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        print("\n")


# Create a new linked list
dllist = CircularDoublyLinkedList()

# Append some nodes to the list
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

# Print the list
dllist.print_list()  # Output: 1 2 3 4

# Prepend a node to the list
dllist.prepend(0)

# Print the list again
dllist.print_list()  # Output: 0 1 2 3 4

# Delete a node from the list
dllist.delete(2)

# Print the list again
dllist.print_list()  # Output: 0 1 3 4
