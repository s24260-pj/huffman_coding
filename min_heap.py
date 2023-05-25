class MinHeap:
    @staticmethod
    def build_min_heap(arr):
        n = int((len(arr) // 2) - 1)

        for k in range(n, -1, -1):
            MinHeap.__min_heapify(arr, k, len(arr) - 1)

        return arr

    @staticmethod
    def __min_heapify(arr, i, heap_size):
        left_child = MinHeap.__left(i)
        r = MinHeap.__right(i)

        if left_child < heap_size and arr[left_child] < arr[i]:
            smallest = left_child
        else:
            smallest = i

        if r < heap_size and arr[r] < arr[smallest]:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            MinHeap.__min_heapify(arr, smallest, heap_size)

    @staticmethod
    def __left(i):
        return 2 * i + 1

    @staticmethod
    def __right(i):
        return 2 * i + 2
