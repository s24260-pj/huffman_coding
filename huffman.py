from node import Node
from tree import Tree
from min_heap_node import MinHeapNode


class Huffman:
    @staticmethod
    def create_tree(sentence):
        list_of_count_of_letters = Huffman.__get_list_of_count_of_letters(sentence)
        list_of_count_of_letters = Huffman.__create_array(list_of_count_of_letters)
        array_of_nodes = Huffman.__create_array_of_nodes(list_of_count_of_letters)
        array_of_nodes = MinHeapNode.build_min_heap(array_of_nodes)

        return Tree(array_of_nodes)

    @staticmethod
    def __get_list_of_count_of_letters(text):
        letter_with_count = {}
        for letter in text:
            if letter in letter_with_count:
                letter_with_count[letter] += 1
            else:
                letter_with_count[letter] = 1

        return letter_with_count

    @staticmethod
    def __create_array_of_nodes(array):
        array_of_nodes = []
        for letter in array:
            array_of_nodes.append(Node(letter[0], letter[1], None, None))
        return array_of_nodes

    @staticmethod
    def __create_array(list_of_count_of_letters):
        array_of_arrays = []

        for key, value in list_of_count_of_letters.items():
            array_of_arrays.append([key, value])

        return array_of_arrays
