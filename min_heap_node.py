class MinHeapNode:
    @staticmethod
    def build_min_heap(arr):
        n = int((len(arr) // 2) - 1)

        for k in range(n, -1, -1):
            MinHeapNode.min_heapify_node(arr, k)

        return arr

    @staticmethod
    def build_min_heap_using_nodes(array_of_nodes):
        return MinHeapNode.build_min_heap(array_of_nodes)

    @staticmethod
    def min_heapify_node(arr, i):
        left_child = MinHeapNode.__left(i)
        r = MinHeapNode.__right(i)

        if left_child < len(arr) and arr[left_child].value < arr[i].value:
            smallest = left_child
        else:
            smallest = i

        if r < len(arr) and arr[r].value < arr[smallest].value:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            MinHeapNode.min_heapify_node(arr, smallest)

    @staticmethod
    def insert_node(arr, node):
        n = len(arr)
        arr.append(node)
        MinHeapNode.__heapify(arr, n, n - 1)

    @staticmethod
    def __heapify(arr, n, i):
        parent = int(((i - 1) / 2))

        if arr[parent].value > 0:
            if arr[i].value > arr[parent].value:
                arr[i], arr[parent] = arr[parent], arr[i]

                MinHeapNode.__heapify(arr, n, parent)

    @staticmethod
    def __left(i):
        return 2 * i + 1

    @staticmethod
    def __right(i):
        return 2 * i + 2
