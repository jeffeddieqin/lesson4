from line_profiler import LineProfiler

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[(low + high) // 2]
        left = low
        right = high
        while True:
            while items[left] < pivot:
                left += 1
            while items[right] > pivot:
                right -= 1
            if left >= right:
                return right
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1

    _quick_sort(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    import random
    data = [random.randint(0, 10000) for _ in range(1000)]

    # 使用 LineProfiler
    lp = LineProfiler()
    lp.add_function(insertion_sort)
    lp.add_function(quick_sort)

    lp_wrapper = lp(insertion_sort)
    lp_wrapper(data)
    lp.print_stats()

    lp_wrapper = lp(quick_sort)
    lp_wrapper(data)
    lp.print_stats()
