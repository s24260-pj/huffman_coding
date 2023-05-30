class CodeCreator:
    @staticmethod
    def create_code_array(code_array, node_object, value):
        if node_object.left_child is None:
            code_array[node_object.key] = value
            return
        else:
            CodeCreator.create_code_array(code_array, node_object.left_child, value + "0")

        if node_object.right_child is None:
            code_array[node_object.key] = value
            return
        else:
            CodeCreator.create_code_array(code_array, node_object.right_child, value + "1")
