import time


def bubble_sort(arr):
    """Bubble Sort: O(n^2) worst/average, O(n) best with early exit."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    """Selection Sort: O(n^2) time across all cases."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    """Insertion Sort: O(n^2) worst/average, O(n) best."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    """Merge Sort: O(n log n) time, O(n) auxiliary space."""
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def measure_avg_time_us(sort_func, base_array, runs=5):
    """Run sort_func `runs` times and return average execution time in microseconds."""
    total_time = 0.0
    for _ in range(runs):
        data = base_array.copy()
        start = time.perf_counter()
        result = sort_func(data)
        end = time.perf_counter()
        assert result == sorted(base_array), "Sorting failed!"
        total_time += (end - start)
    return (total_time / runs) * 1e6  # microseconds


def main():
    arr1 = list(range(1, 6))     # N = 5
    arr2 = list(range(1, 11))    # N = 10
    arr3 = list(range(1, 51))    # N = 50
    arr4 = list(range(1, 101))   # N = 100

    datasets = [(5, arr1), (10, arr2), (50, arr3), (100, arr4)]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }

    print(f"{'N':<6} | {'Bubble (us)':<14} | {'Selection (us)':<16} | {'Insertion (us)':<16} | {'Merge (us)':<14}")
    print("-" * 78)
    for n, arr in datasets:
        row = {name: measure_avg_time_us(fn, arr, runs=5) for name, fn in algorithms.items()}
        print(
            f"{n:<6} | {row['Bubble Sort']:<14.2f} | {row['Selection Sort']:<16.2f} "
            f"| {row['Insertion Sort']:<16.2f} | {row['Merge Sort']:<14.2f}"
        )


if __name__ == "__main__":
    main()
