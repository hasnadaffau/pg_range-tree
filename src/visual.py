import matplotlib.pyplot as plt

# def plot_points(points, query_result=None, x_range=None, y_range=None):
#     """
#     Visualisasi titik-titik dan hasil query (jika ada)
#     """
#     xs, ys = zip(*points)
#     plt.figure(figsize=(6, 6))
#     plt.scatter(xs, ys, c='blue', label='All Points')

#     if query_result:
#         qx, qy = zip(*query_result)
#         plt.scatter(qx, qy, c='red', label='Query Result')

#     if x_range and y_range:
#         rect = plt.Rectangle((x_range[0], y_range[0]),
#                              x_range[1] - x_range[0],
#                              y_range[1] - y_range[0],
#                              edgecolor='green',
#                              facecolor='none',
#                              linewidth=2,
#                              label='Query Range')
#         plt.gca().add_patch(rect)

#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.legend()
#     plt.grid(True)
#     plt.title("2D Range Tree Points & Query Result")
#     plt.show()

import matplotlib.pyplot as plt


def plot_points(points, query_result=None, x_range=None, y_range=None,
                default_size=6, max_size=10):

    xs, ys = zip(*points)

    size = default_size
    max_dim = max(max(xs) - min(xs), max(ys) - min(ys))
    if max_dim > default_size:
        size = min(max_dim, max_size)

    fig, ax = plt.subplots(figsize=(size, size))

    # Plot node
    ax.scatter(xs, ys,
               s=30,
               alpha=0.4,
               marker='o',
               label=f'All Points ({len(points)})')

    # Plot query 
    if query_result:
        qx, qy = zip(*query_result)
        ax.scatter(qx, qy,
                   s=100,
                   facecolors='none',
                   edgecolors='red',
                   linewidths=1.5,
                   marker='o',
                   label=f'Query Result ({len(query_result)})')

    # Plot rectangle query
    if x_range and y_range:
        rect = plt.Rectangle((x_range[0], y_range[0]),
                             x_range[1] - x_range[0],
                             y_range[1] - y_range[0],
                             edgecolor='green',
                             facecolor='none',
                             linewidth=2,
                             linestyle='--',
                             label='Query Range')
        ax.add_patch(rect)
        # Set limits 
        min_x = min(min(xs), x_range[0]) - 1
        max_x = max(max(xs), x_range[1]) + 1
        min_y = min(min(ys), y_range[0]) - 1
        max_y = max(max(ys), y_range[1]) + 1
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)
    else:
        ax.margins(0.05)

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.grid(color='gray', linestyle=':', linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_visible(True)

    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

    plt.title("2D Range Tree Visualization")
    plt.tight_layout()
    plt.show()
    
from graphviz import Digraph

def visualize_tree_radial(node, graph=None):
    if graph is None:
        graph = Digraph(format='png',
                        graph_attr={"rankdir": "TB", "bgcolor": "#1e1e1e"},
                        node_attr={'fontcolor': 'white', 'color': 'white', 'style': 'filled', 'fillcolor': '#2d2d2d', 'fontname': 'Helvetica'},
                        edge_attr={'color': 'white'})

    if node is None:
        return graph

    if isinstance(node.val, tuple):
        node_label = f"{node.val[0]},{node.val[1]}"
    else:
        node_label = str(node.val)

    graph.node(str(node.id), node_label)

    for child in [node.left, node.right]:
        if child is not None:
            if isinstance(child.val, tuple):
                child_label = f"{child.val[0]},{child.val[1]}"
            else:
                child_label = str(child.val)

            graph.node(str(child.id), child_label)
            graph.edge(str(node.id), str(child.id))
            visualize_tree_radial(child, graph)

    return graph
