from node import Node
from min_heap import MinHeap


class Tree:
    def __init__(self, array):
        self.roots = self.__make(array)

    def __make(self, array_of_elements):
        if len(array_of_elements) == 1:
            return array_of_elements[0]

        left_child = array_of_elements[0]
        right_child = array_of_elements[1]

        new_node_key = left_child.key + right_child.key
        new_node_value = left_child.value + right_child.value

        new_element = Node(new_node_key, new_node_value, left_child, right_child)

        array_of_elements.pop(0)
        array_of_elements.pop(0)

        array_of_elements.append(new_element)
        array_of_elements = MinHeap.build_min_heap(array_of_elements)

        return self.__make(array_of_elements)
