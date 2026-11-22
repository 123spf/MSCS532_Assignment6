# MSCS 532 – Assignment 6

This repository contains my Python implementations and analysis for **Part 1 (Medians and Order Statistics)** and **Part 2 (Elementary Data Structures)**.

## How to Run the Code

Requires **Python 3** (no external libraries needed). Open a terminal inside the `MSCS532_Assignment6` folder and run:

```
# Part 1: Selection algorithms & benchmarks
python3 selection.py
python3 benchmark_selection.py

# Part 2: Elementary data structures
python3 arrays_and_matrices.py
python3 stacks_and_queues.py
python3 linked_list.py

```

## Summary of Findings

### Part 1: Selection Algorithms

* **Linear scaling:** Both Randomized Quickselect (`RANDOMIZED-SELECT`) and Deterministic Median of Medians (`SELECT`) scaled linearly ($O(n)$) as array sizes grew from $1,000$ to $20,000$ across random, sorted, reverse-sorted, and duplicate-heavy inputs.

* **Practical speed:** Randomized Quickselect ran over twice as fast on random and duplicate-heavy arrays because Median of Medians carries higher constant-factor overhead from grouping and sorting.

* **Sorted inputs & duplicates:** On sorted and reverse-sorted arrays, Median of Medians nearly matched Quickselect because its strided 5-element grouping landed directly on the median on the first partition. Pairing each value with its original index—$(A[i], i)$—kept duplicate-heavy arrays from degrading to $O(n^2)$.

### Part 2: Elementary Data Structures

* **Arrays & Matrices:** Contiguous memory provides $O(1)$ access by index (using row-major indexing for matrices), while ordered insertions and deletions take $O(n)$ worst-case time because elements must be shifted.

* **Stacks & Queues (Array-Based):** Both the LIFO stack (`push`/`pop`) and circular FIFO queue (`enqueue`/`dequeue`) operate in $O(1)$ time, with overflow and underflow checks for their fixed capacities.

* **Singly Linked Lists:** Inserting at the front takes $O(1)$ time and allows dynamic growth, while searching, traversing, and deleting by key take $O(n)$ worst-case time because nodes only store `next` pointers.