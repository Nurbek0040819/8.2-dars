class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Invalid position")

        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Position out of bounds")

        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        deleted_node = self.head
        self.head = self.head.next
        deleted_node.next = None  

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        deleted_node.next = None  

    def delete_at_position(self, position):
        if position < 0:
            raise ValueError("Invalid position")

        if self.head is None:
            return

        if position == 0:
            self.delete_at_beginning()
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise IndexError("Position out of bounds")

        deleted_node = current.next
        current.next = deleted_node.next
        deleted_node.next = None  

    def get_sum(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def get_mean(self):
        total_sum = self.get_sum()
        if total_sum == 0:
            raise ZeroDivisionError("List is empty")
        return total_sum / self.get_length()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_duplicates(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node and next_node.data == current.data:
                next_node = next_node.next
            current.next = next_node
            current = current.next

    def create_from_list(self, data_list):
        for data in data_list[::-1]:  
            self.insert_at_beginning(data)

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        return result

# Example usage
linked_list = LinkedList()
linked_list.create_from_list([5, 3, 8, 2, 1, 3])  
print(linked_list)  
