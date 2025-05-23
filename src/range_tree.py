# src/range_tree.py

from src.node import create_node

def split_in_half(points, alignment=True):
    key = 0 if alignment else 1
    points = sorted(points, key=lambda p: p[key])
    mid = (len(points) + 1) // 2
    return {
        "mid": mid - 1,
        "left_half": points[:mid],
        "right_half": points[mid:]
    }

def build_2d_range_tree(points, alignment=True, parent=None):
    if len(points) == 1:
        leaf = create_node(True, points[0])
        leaf.parent = parent
        return leaf
    else:
        split_result = split_in_half(points, alignment)
        mid_val = split_result['left_half'][-1][0] if alignment else split_result['left_half'][-1][1]
        node = create_node(False, mid_val)
        node.parent = parent
        node.left = build_2d_range_tree(split_result['left_half'], alignment, node)
        node.right = build_2d_range_tree(split_result['right_half'], alignment, node)
        if alignment:
            node.assoc = build_2d_range_tree(points, alignment=False)
        else:
            node.assoc = None
        return node

def range_query(node, x_range, y_range):
    x_min, x_max = x_range
    y_min, y_max = y_range

    def search_y(node, y_min, y_max):
        if node is None:
            return []
        if node.is_leaf:
            x, y = node.val
            if y_min <= y <= y_max and x_min <= x <= x_max:
                return [node.val]
            else:
                return []
        if node.val < y_min:
            return search_y(node.right, y_min, y_max)
        elif node.val > y_max:
            return search_y(node.left, y_min, y_max)
        else:
            return search_y(node.left, y_min, y_max) + search_y(node.right, y_min, y_max)

    def query_2d(node, x_min, x_max, y_min, y_max):
        if node is None:
            return []
        if node.is_leaf:
            x, y = node.val
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return [node.val]
            else:
                return []
        if node.val < x_min:
            return query_2d(node.right, x_min, x_max, y_min, y_max)
        elif node.val > x_max:
            return query_2d(node.left, x_min, x_max, y_min, y_max)
        else:
            left_res = query_2d(node.left, x_min, x_max, y_min, y_max)
            right_res = query_2d(node.right, x_min, x_max, y_min, y_max)
            assoc_res = []
            if node.assoc is not None:
                assoc_res = search_y(node.assoc, y_min, y_max)
            filtered_assoc = [p for p in assoc_res if x_min <= p[0] <= x_max and y_min <= p[1] <= y_max]
            combined = set(left_res + right_res + filtered_assoc)
            return list(combined)

    return query_2d(node, x_min, x_max, y_min, y_max)
