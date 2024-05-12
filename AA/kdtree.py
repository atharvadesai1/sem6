class Tree:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

class KDTree:
    def __init__(self,n):
        self.n = n
        self.root = None
        self.flag = True

    def insert(self, value):
        if self.flag:
            root_node = Tree()
            root_node.val = value
            self.root = root_node
            self.flag = False
        else:
            inserted_node = Tree()
            inserted_node.val = value
            current_node = self.root
            inserted = False
            k = 0
            while not inserted:
                if inserted_node.val[k] < current_node.val[k]:
                    if not current_node.left:
                        current_node.left = inserted_node
                        inserted = True
                    else:
                        k = (k+1)%self.n
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = inserted_node
                        inserted = True
                    else:
                        k = (k+1)%self.n
                        current_node = current_node.right
        
    def display(self, root_node, level=0, prefix="Root: "):
        if root_node:
            print(str(level) + ' ' + str(prefix) + ' '+str(root_node.val))  
            self.display(root_node.left, level + 1, "L: ")  
            self.display(root_node.right, level + 1, "R: ")  

points = [
    (5, 4, 7),
    (2, 3, 4),       
    (9, 6, 2),    
    (4, 7, 8),    
    (8, 1, 5),    
    (7, 2, 6)     
]

n = 3
kd = KDTree(n)

for value in points:
    kd.insert(value)
print('******************DISPLAYING KD-TREE******************')
print()
root_node = kd.root
kd.display(root_node)
