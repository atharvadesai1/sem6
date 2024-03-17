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
            if self.head is None:  # If the tree is empty
                inserted_node.parent = None  # Set the parent to None
                self.head = inserted_node
            else:
                self.check_condition(inserted_node, self.head)

    def check_condition(self, inserted_node, current):
        uncle_color = 'b'  # Default uncle color
        while current:
            if inserted_node.val < current.val:
                if not current.left and current.color == 'b':
                    current.left = inserted_node
                    inserted_node.parent = current
                    inserted_node.direction = 'L'
                    break
                elif not current.left and current.color == 'r':  # Red-Red conflict
                    current.left = inserted_node
                    inserted_node.parent = current
                    inserted_node.direction = 'L'
                    if current.parent and current.parent.left == current:
                        uncle = current.parent.right
                        if uncle and uncle.color == 'r':
                            uncle_color = 'r'
                    self.operation = current.direction + inserted_node.direction + uncle_color
                    break
                else:
                    current = current.left
            else:
                if not current.right and current.color == 'b':
                    current.right = inserted_node
                    inserted_node.parent = current
                    inserted_node.direction = 'R'
                    break
                elif not current.right and current.color == 'r':  # Red-Red conflict
                    current.right = inserted_node
                    inserted_node.parent = current
                    inserted_node.direction = 'R'
                    if current.parent and current.parent.right == current:
                        uncle = current.parent.left
                        if uncle and uncle.color == 'r':
                            uncle_color = 'r'
                    self.operation = str(current.direction) + str(inserted_node.direction) + str(uncle_color)
                    break
                else:
                    current = current.right


        #checking which opertion it belongs to
        parents = inserted_node.parent
        grandparents = parents.parent
        if self.operation == 'RRr':
            parents.color = 'b'
            grandparents.color = 'r'
            uncle.color = 'b'
        elif self.operation == 'LLr':
            parents.color = 'b'
            grandparents.color = 'r'
            uncle.color = 'b'
        elif self.operation == 'RLr':
            parents.color = 'b'
            grandparents.color = 'r'
            uncle.color = 'b'
        elif self.operation == 'LRr':
            parents.color = 'b'
            grandparents.color = 'r'
            uncle.color = 'b'
        elif self.operation == 'RRb':
            parents.parent = grandparents.parent
            parents.left = grandparents
            parents.color = 'b'
            parents.direction = grandparents.direction
            grandparents.parent = parents
            grandparents.color = 'r'
            grandparents.direction = 'L'

        elif self.operation == 'LLb':
            parents.parent = grandparents.parent
            parents.right = grandparents
            parents.color = 'b'
            parents.direction = grandparents.direction
            grandparents.parent = parents
            grandparents.color = 'r'
            grandparents.direction = 'R'
        elif self.operation == 'RLb':
            inserted_node.color = 'b'
            inserted_node.right = parents
            inserted_node.left = grandparents
            inserted_node.parent = grandparents.parent
            parents.left = None
            parents.parent = inserted_node
            grandparents.right = None
            grandparents.parent = inserted_node
            grandparents.color = 'r'
        elif self.operation == 'LRb':
            inserted_node.color = 'b'
            inserted_node.left = parents
            inserted_node.right = grandparents
            inserted_node.parent = grandparents.parent
            parents.right = None
            parents.parent = inserted_node
            grandparents.left = None
            grandparents.parent = inserted_node
            grandparents.color = 'r'
        else:
            pass
        self.operation = ''
        print(f'Node {inserted_node.val} inserted successfully')


    def display(self, current_node, level):
        if current_node is not None:
            self.display(current_node.right, level + 1)
            print("  " * level + str(current_node.val) + str(current_node.color))
            self.display(current_node.left, level + 1)


        
elements = [12,20,9,17,18,32,27,42,80,4,2]
root = Node('b', elements[0])
rbtinsert = RbtInsertion()
rbtinsert.insert(root)

for i in range(1,len(elements)):
    new_node = Node('r',elements[i])
    rbtinsert.insert(new_node)   

# rbtinsert.display(root, 0)




