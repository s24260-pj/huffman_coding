from node import Node
from tree import Tree
from min_heap_node import MinHeapNode
from code_creator_service import CodeCreator
from text_changer_service import TextChanger
from text_huffman_decoder_service import TextHuffmanDecoder


class Huffman:
    @staticmethod
    def create_tree(sentence):
        list_of_count_of_letters = Huffman.__get_list_of_count_of_letters(sentence)
        array_of_nodes = Huffman.__create_array_of_nodes(list_of_count_of_letters)
        array_of_nodes = MinHeapNode.build_min_heap(array_of_nodes)

        return Tree(array_of_nodes)

    @staticmethod
    def create_code_array(tree):
        code_array = {}
        CodeCreator.create_code_array(code_array, tree.roots, "")
        return code_array

    @staticmethod
    def encode_text(sentence, code_array):
        return TextChanger.change(sentence, code_array)

    @staticmethod
    def decode_text(encoded_text, tree):
        return TextHuffmanDecoder.decode(encoded_text, tree.roots)

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
            array_of_nodes.append(Node(letter, array[letter], None, None))
        return array_of_nodes
