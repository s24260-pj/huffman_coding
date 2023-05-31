from huffman import Huffman

sentence = "test ale to nie jest test"

tree = Huffman.create_tree(sentence)
code_array = Huffman.create_code_array(tree)
encoded_text = Huffman.encode_text(sentence, code_array)
decoded_text = Huffman.decode_text(encoded_text, tree)

print(code_array)
print(encoded_text)
print(decoded_text)
