class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def find_middle_value(self):
        ##########################
        ##
        ##
        ##
        ##
        ##########################

def read_values_from_file(filename):
    ll = LinkedList()
    with open(filename, 'r') as file:
        values_line = file.readline()
        values = values_line.strip().split(' ')  
        for value in values:
            ll.append(int(value))
    return ll


filename = 'list_values.txt'  # Pieņem, ka vērtības ir saglabātas šajā failā vienā rindā
linked_list = read_values_from_file(filename)
middle_value = linked_list.find_middle_value()
print("Vidējā elementa vērtība:", middle_value)

