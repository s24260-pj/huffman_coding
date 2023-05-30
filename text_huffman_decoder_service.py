class TextHuffmanDecoder:
    @staticmethod
    def decode(coded_sentence, roots):
        node = roots
        decoded_sequence = ""
        for letter in coded_sentence:
            if letter == '0' and node.left_child is not None:
                node = node.left_child

            if letter == '1' and node.right_child is not None:
                node = node.right_child

            if node.right_child is None and node.left_child is None:
                decoded_sequence += node.key
                node = roots

        return decoded_sequence
