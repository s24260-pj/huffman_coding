from huffman import Huffman

sentence = "test ale to nie jest test"
tree = Huffman.create_tree(sentence)

code_array = {}


def create_code_array(node_object, value):
    if node_object.left_child is None:
        code_array[node_object.key] = value
        return
    else:
        create_code_array(node_object.left_child, value + "0")

    if node_object.right_child is None:
        code_array[node_object.key] = value
        return
    else:
        create_code_array(node_object.right_child, value + "1")


create_code_array(tree.roots, "")

print(code_array)
