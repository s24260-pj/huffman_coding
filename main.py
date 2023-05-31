import os
from huffman import Huffman

file_name = "julian_tuwim_abecadlo.txt"
new_file_name = "encoded_text.txt"
# get resource from file
file = open(file_name, "r")
sentence = file.read()
file.close()

file_stats = os.stat(file_name)
print(f'File Size in Bytes is {file_stats.st_size}')

# huffman coding
tree = Huffman.create_tree(sentence)
code_array = Huffman.create_code_array(tree)
encoded_text = Huffman.encode_text(sentence, code_array)
decoded_text = Huffman.decode_text(encoded_text, tree)

# create new file
new_file = open(new_file_name, "a")
new_file.write(f'{code_array}')
new_file.write('\n')
new_file.write(encoded_text)
new_file.close()

new_file_stats = os.stat(new_file_name)
print(f'File Size in Bytes is {new_file_stats.st_size}')
