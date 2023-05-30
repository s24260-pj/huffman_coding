from huffman import Huffman
from code_creator_service import CodeCreator
from text_changer_service import TextChanger
from text_huffman_decoder_service import TextHuffmanDecoder

sentence = "test ale to nie jest test"
tree = Huffman.create_tree(sentence)

code_array = {}
CodeCreator.create_code_array(code_array, tree.roots, "")

coded_text = TextChanger.change(sentence, code_array)
print(coded_text)
decoded_text = TextHuffmanDecoder.decode(coded_text, tree.roots)
print(decoded_text)
