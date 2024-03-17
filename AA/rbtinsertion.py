class Node:
    def __init__(self, color: str, val: int):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        self.direction = None

class RbtInsertion:
    def __init__(self):
        self.head = None
        self.operation = None

    def insert(self, inserted_node):
        if inserted_node.color == 'b':
            self.head = inserted_node
        else:
            self.check_condition(inserted_node, self.head)

    def check_condition(self, inserted_node, current):
        if inserted_node.val < current.val:
            if not current.left and current==self.head:
                current.left = inserted_node
                inserted_node.parent = current
                inserted_node.direction = 'L'
            elif not current.left:
                current.left = inserted_node
                inserted_node.parent = current
                inserted_node.direction = 'L'
                if inserted_node.parent.direction == 'L':
                    uncle = inserted_node.parent.parent.right
                    if not uncle:
                        uncle_color = 'b'
                    if uncle.color == 'r':
                        uncle_color = 'r'
                    else:
                        uncle_color = 'b'
                self.operation = inserted_node.parent.direction + inserted_node.direction + uncle_color
                    
                
            else:
                current = current.left
                self.check_condition(inserted_node, current)
        elif inserted_node.val > current.val:
            if not current.left and current==self.head:
                current.right = inserted_node

        #checking which opertion it belongs to
        if self.operation == 'RRr':
            pass
        elif self.operation == 'LLr':
            pass
        elif self.operation == 'RLr':
            pass
        elif self.operation == 'LRr':
            pass
        elif self.operation == 'RRb':
            pass
        elif self.operation == 'LLb':
            pass
        elif self.operation == 'RLb':
            pass
        elif self.operation == 'LRb':
            pass


        


    def display(self):
        pass

elements = [12,20,9,17,18,32,27,42,80,4,2]
root = Node('b', elements[0])
rbtinsert = RbtInsertion()
rbtinsert.insert(root)

for i in range(1,len(elements)):
    new_node = Node('r',elements[i])
    rbtinsert.insert(new_node)





