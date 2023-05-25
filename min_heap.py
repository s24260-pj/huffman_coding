class MinHeap:
    @staticmethod
    def build_min_heap(arr):
        n = int((len(arr) // 2) - 1)

        for k in range(n, -1, -1):
            MinHeap.__min_heapify(arr, k)

        return arr

    @staticmethod
    def build_min_heap_using_nodes(array_of_nodes):
        tmp_array = []
        for node in array_of_nodes:
            tmp_array.append([node.key, node.value])

        tmp_array = MinHeap.build_min_heap(tmp_array)

        return sorted(array_of_nodes, key=lambda x: [element[0] for element in tmp_array].index(x.key))

    @staticmethod
    def __min_heapify(arr, i):
        left_child = MinHeap.__left(i)
        r = MinHeap.__right(i)

        if left_child < len(arr) and arr[left_child][1] < arr[i][1]:
            smallest = left_child
        else:
            smallest = i

        if r < len(arr) and arr[r][1] < arr[smallest][1]:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            MinHeap.__min_heapify(arr, smallest)

    @staticmethod
    def __left(i):
        return 2 * i + 1

    @staticmethod
    def __right(i):
        return 2 * i + 2
