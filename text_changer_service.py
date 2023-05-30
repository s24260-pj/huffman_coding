class TextChanger:
    @staticmethod
    def change(sentence, code_array):
        for key in code_array:
            sentence = sentence.replace(key, code_array[key])
        return sentence
