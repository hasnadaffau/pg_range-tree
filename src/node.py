# src/node.py

leaf_node_id_map = {}
leaf_id_counter = -1

class Node:
    def __init__(self, is_leaf, val, left=None, right=None, assoc=None, parent=None):
        self.is_leaf = is_leaf
        self.val = val          
        self.left = left
        self.right = right
        self.assoc = assoc      
        self.parent = parent
        self.id = id(self)      
        self.leaf_id = None    

    def __repr__(self):
        if self.is_leaf:
            return f"LeafNode({self.val})"
        else:
            return f"InternalNode({self.val})"

def create_node(is_leaf, val, left=None, right=None, assoc=None, parent=None):
    global leaf_id_counter
    node = Node(is_leaf, val, left, right, assoc, parent)
    if is_leaf:
        leaf_key = f"{val[0]};{val[1]}"
        if leaf_key in leaf_node_id_map:
            node.leaf_id = leaf_node_id_map[leaf_key]
        else:
            node.leaf_id = leaf_id_counter
            leaf_node_id_map[leaf_key] = leaf_id_counter
            leaf_id_counter -= 1
    return node
