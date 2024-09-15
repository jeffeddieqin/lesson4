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
from memory_profiler import profile

@profile
def mem_profiled_insertion_sort(arr):
    insertion_sort(arr)

@profile
def mem_profiled_quick_sort(arr):
    quick_sort(arr)

if __name__ == '__main__':
    import random
    data = [random.randint(0, 10000) for _ in range(1000)]
    
    mem_profiled_insertion_sort(data)
    mem_profiled_quick_sort(data)
