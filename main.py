import os
from huffman import Huffman
from ascii_code_generator import AsciiCodeGenerator

file_name = "long_lorem_ipsum.txt"
new_file_name = "encoded_text.txt"

# get resource from file
file = open(file_name, "r")
sentence = file.read()
file.close()

file_stats = os.stat(file_name)
print(f'File Without encode Size in Bytes is {file_stats.st_size}')

# huffman coding
tree = Huffman.create_tree(sentence)
code_array = Huffman.create_code_array(tree)
encoded_text = Huffman.encode_text(sentence, code_array)
encoded_text_ascii = AsciiCodeGenerator.generate(encoded_text)

decoded_text = Huffman.decode_text(encoded_text, tree)

# create new file
new_file = open(new_file_name, "a")
new_file.write(f'{code_array}')
new_file.write('\n')
new_file.write(encoded_text_ascii)
new_file.close()

new_file_stats = os.stat(new_file_name)
print(f'File Size in Bytes is {new_file_stats.st_size}')
