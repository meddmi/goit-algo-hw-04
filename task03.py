"""Compare insertion sort, merge sort, and Python's built-in Timsort."""

import random
import timeit
from collections.abc import Callable

Sorter = Callable[[list], list]
Dataset = tuple[str, list]
RANDOM_SEED = 45


def insertion_sort(values: list) -> list:
    """Sort a list using the insertion sort algorithm."""
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values


def merge_sort(values: list) -> list:
    """Sort a list using the merge sort algorithm."""
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left_half = values[:mid]
    right_half = values[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    merged: list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def timsort(values: list) -> list:
    """Sort a list using Python's built-in list.sort method."""
    values.sort()
    return values


def make_dataset(kind: str, size: int) -> list[int]:
    """Generate a dataset of the specified kind and size."""
    rng = random.Random(RANDOM_SEED + size)

    if kind == "random":
        return [rng.randint(0, size * 10) for _ in range(size)]

    if kind == "reversed":
        return list(range(size, 0, -1))

    if kind == "many_duplicates":
        return [rng.randint(0, 20) for _ in range(size)]

    raise ValueError(f"Unknown dataset kind: {kind}")


def measure_sorting_time(sorter: Sorter, values: list) -> float:
    """Return the best execution time from several timeit runs."""
    execution_time = timeit.timeit(lambda: sorter(values.copy()), number=1)
    return execution_time


def print_table_header() -> None:
    """Print benchmark table header."""
    print(f"{'Dataset':<18} {'Size':>8} {'Algorithm':<15} {'Time, sec':>12}")
    print("-" * 57)


def print_benchmark_result(
    dataset_name: str,
    size: int,
    algorithm_name: str,
    sorting_time: float | None,
) -> None:
    """Print a single benchmark row."""
    if sorting_time is None:
        formatted_time = "skipped"
    else:
        formatted_time = f"{sorting_time:.6f}"

    print(f"{dataset_name:<18} {size:>8} {algorithm_name:<15} {formatted_time:>12}")


def main() -> None:
    """Start the sorting algorithm comparison."""
    dataset_kinds = [
        "random",
        "reversed",
        "many_duplicates",
    ]

    sorters: list[tuple[str, Sorter]] = [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Timsort", timsort),
    ]

    print_table_header()

    for size in [1000, 5000, 10_000]:
        for kind in dataset_kinds:
            dataset = make_dataset(kind, size)

            for algorithm_name, sorter in sorters:
                sorting_time = measure_sorting_time(sorter, dataset)
                print_benchmark_result(kind, size, algorithm_name, sorting_time)


if __name__ == "__main__":
    main()
