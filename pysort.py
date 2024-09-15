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
import cProfile

def test_sort(sort_func, data):
    print(f"Sorting using {sort_func.__name__}")
    cProfile.runctx(f'{sort_func.__name__}(data.copy())', globals(), locals())

if __name__ == '__main__':
    import random
    data = [random.randint(0, 10000) for _ in range(1000)]
    
    test_sort(insertion_sort, data)
    test_sort(quick_sort, data)
