from node import Node
from min_heap import MinHeap


class Tree:
    def __init__(self, array):
        self.roots = self.__make(array)

    def __make(self, array_of_elements):
        if len(array_of_elements) == 1:
            return array_of_elements[0]

        # get first head
        first_head_element = array_of_elements.pop(0)
        array_of_elements.insert(0, array_of_elements.pop())
        array_of_elements = MinHeap.build_min_heap_using_nodes(array_of_elements)

        # get second head
        second_head_element = array_of_elements.pop(0)
        if len(array_of_elements) > 0:
            array_of_elements.insert(0, array_of_elements.pop())
            array_of_elements = MinHeap.build_min_heap_using_nodes(array_of_elements)

        # create new node
        new_node_key = first_head_element.key + second_head_element.key
        new_node_value = first_head_element.value + second_head_element.value
        new_element = Node(new_node_key, new_node_value, first_head_element, second_head_element)
        array_of_elements.append(new_element)

        return self.__make(array_of_elements)
