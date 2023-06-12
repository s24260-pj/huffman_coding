class AsciiCodeGenerator:
    @staticmethod
    def generate(bit_code):
        ascii_code = ""

        for i in range(0, len(bit_code), 8):
            fragment = bit_code[i:i + 8]
            decimal = int(fragment, 2)
            ascii_code += chr(decimal)

        return ascii_code
