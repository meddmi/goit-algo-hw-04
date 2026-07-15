# goit-algo-hw-04

Homework project for algorithm practice. The repository contains three independent
Python scripts:

- `task01.py` - recursively copies files from a source directory into folders
  grouped by file extension.
- `task02.py` - draws a Koch snowflake with a user-selected recursion level.
- `task03.py` - compares insertion sort, merge sort, and Python's built-in
  Timsort implementation.

`colorized_logger.py` contains small helper functions for colored terminal
messages used by the first two tasks.

## Task 01. Recursive File Copying

`task01.py` recursively reads a source directory and copies every regular file
to a destination directory. Files are grouped into subdirectories by extension:

- files with `.txt` go to `txt/`;
- files with `.jpg` go to `jpg/`;
- files without an extension go to `no_extension/`.

The script skips common system files such as `.DS_Store` and `Thumbs.db`. If a
file with the same name already exists in the target extension directory, the
script adds a numeric suffix instead of overwriting it.

Run:

```bash
python3 task01.py <source_directory> [destination_directory]
```

If `destination_directory` is not provided, the script uses `dist`.

## Task 02. Koch Snowflake

`task02.py` uses the standard `turtle` module to draw a Koch snowflake. The user
enters the recursion level in the terminal. Valid values are integers from `0`
to `5`.

Run:

```bash
python3 task02.py
```

The script opens a turtle graphics window and draws three Koch curve sides to
form the snowflake.

## Task 03. Sorting Algorithm Comparison

`task03.py` compares three sorting algorithms:

- insertion sort;
- merge sort;
- Python's built-in `list.sort`, which uses Timsort.

The `timeit` module is used to measure execution time. Each algorithm runs on a
copy of the same dataset, so the comparison conditions are identical and the
original dataset is not modified between algorithms. The script repeats each
measurement three times and prints the best result.

Test datasets:

- random integers;
- reversed integers;
- many duplicated integers.

Dataset sizes:

- `1_000`;
- `5_000`;
- `10_000`.

Run:

```bash
python3 task03.py
```

### Benchmark Results

Times are shown in seconds. Results may differ slightly depending on the
computer and current system load.

```text
Dataset                Size Algorithm          Time, sec
---------------------------------------------------------
random                 1000 Insertion Sort      0.009212
random                 1000 Merge Sort          0.000999
random                 1000 Timsort             0.000112
sorted                 1000 Insertion Sort      0.000056
sorted                 1000 Merge Sort          0.000747
sorted                 1000 Timsort             0.000005
reversed               1000 Insertion Sort      0.017486
reversed               1000 Merge Sort          0.001082
reversed               1000 Timsort             0.000007
nearly_sorted          1000 Insertion Sort      0.000315
nearly_sorted          1000 Merge Sort          0.000806
nearly_sorted          1000 Timsort             0.000021
many_duplicates        1000 Insertion Sort      0.008487
many_duplicates        1000 Merge Sort          0.000917
many_duplicates        1000 Timsort             0.000077
random                 5000 Insertion Sort      0.227706
random                 5000 Merge Sort          0.005930
random                 5000 Timsort             0.000483
sorted                 5000 Insertion Sort      0.000253
sorted                 5000 Merge Sort          0.004540
sorted                 5000 Timsort             0.000027
reversed               5000 Insertion Sort      0.449313
reversed               5000 Merge Sort          0.004477
reversed               5000 Timsort             0.000033
nearly_sorted          5000 Insertion Sort      0.005992
nearly_sorted          5000 Merge Sort          0.004955
nearly_sorted          5000 Timsort             0.000086
many_duplicates        5000 Insertion Sort      0.213347
many_duplicates        5000 Merge Sort          0.005176
many_duplicates        5000 Timsort             0.000350
random                10000 Insertion Sort      0.927817
random                10000 Merge Sort          0.012116
random                10000 Timsort             0.001094
sorted                10000 Insertion Sort      0.000489
sorted                10000 Merge Sort          0.009400
sorted                10000 Timsort             0.000057
reversed              10000 Insertion Sort      1.794054
reversed              10000 Merge Sort          0.009580
reversed              10000 Timsort             0.000066
nearly_sorted         10000 Insertion Sort      0.028771
nearly_sorted         10000 Merge Sort          0.010204
nearly_sorted         10000 Timsort             0.000173
many_duplicates       10000 Insertion Sort      0.842201
many_duplicates       10000 Merge Sort          0.011056
many_duplicates       10000 Timsort             0.000679
```

### Conclusions

Insertion sort has `O(n^2)` complexity in the average and worst cases, and
`O(n)` complexity in the best case. The benchmark confirms this: insertion sort
is very fast on already sorted and nearly sorted data, but its time grows sharply
on random, reversed, and duplicate-heavy datasets.

Merge sort has stable `O(n log n)` complexity across the tested input types. Its
execution time grows much more slowly than insertion sort, so it is
significantly more efficient on larger datasets.

Timsort, used by Python's `sorted` and `list.sort`, is the fastest algorithm in
all tests. It combines ideas from merge sort and insertion sort and efficiently
uses existing order in the input. In this benchmark it performs especially well
on sorted, reversed, and nearly sorted datasets, while also remaining fastest
for random and duplicate-heavy data.

Practical conclusion: in most real Python tasks, it is better to use the
built-in `sorted` function or `list.sort` method. They are faster, more reliable,
and better optimized than hand-written implementations of basic sorting
algorithms.
