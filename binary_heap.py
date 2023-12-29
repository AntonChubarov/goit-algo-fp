import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key, index, color="skyblue"):
        self.key = key
        self.index = index
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, heap, pos, parent_index=None, layer=1):
    if parent_index is None:
        parent_index = 0

    if parent_index < len(heap):
        parent = heap[parent_index]
        graph.add_node(parent.id, color=parent.color, label=parent.key)

        left_child_index = 2 * parent_index + 1
        if left_child_index < len(heap):
            left_child = heap[left_child_index]
            graph.add_edge(parent.id, left_child.id)
            pos[left_child.id] = (left_child.index - 1 / (2 ** layer), -layer)
            add_edges(graph, heap, pos, left_child_index, layer=layer + 1)

        right_child_index = 2 * parent_index + 2
        if right_child_index < len(heap):
            right_child = heap[right_child_index]
            graph.add_edge(parent.id, right_child.id)
            pos[right_child.id] = (right_child.index + 1 / (2 ** layer), -layer)
            add_edges(graph, heap, pos, right_child_index, layer=layer + 1)


def draw_heap(heap):
    heap_nodes = [HeapNode(key, index) for index, key in enumerate(heap)]
    heap_graph = nx.DiGraph()
    pos = {node.id: (node.index, 0) for node in heap_nodes}
    add_edges(heap_graph, heap_nodes, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=1000, node_color=colors)
    plt.show()


if __name__ == "__main__":
    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    heapq.heapify(heap)

    draw_heap(heap)
