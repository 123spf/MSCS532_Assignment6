import math
import random


def partition(A, p, r):
    """Rearrange A[p..r] around the last element A[r] and return its new index."""
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            # Swap A[i] and A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    # Put the pivot in its final position
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1


def randomized_partition(A, p, r):
    """Pick a random pivot in A[p..r], move it to the end, and partition."""
    rand_index = random.randint(p, r)

    # Swap the random element with the last element A[r]
    temp = A[rand_index]
    A[rand_index] = A[r]
    A[r] = temp

    return partition(A, p, r)


def partition_around(A, p, r, pivot):
    """Find the chosen pivot in A[p..r], move it to the end, and partition."""
    for index in range(p, r + 1):
        if A[index] == pivot:
            temp = A[index]
            A[index] = A[r]
            A[r] = temp
            break

    return partition(A, p, r)


def randomized_select_helper(A, p, r, i):
    """CLRS Section 9.2: RANDOMIZED-SELECT(A, p, r, i)."""
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select_helper(A, p, q - 1, i)
    else:
        return randomized_select_helper(A, q + 1, r, i - k)


def select_helper(A, p, r, i):
    """CLRS Section 9.3: SELECT(A, p, r, i)."""
    # Shrink the subarray until its length is divisible by 5
    while (r - p + 1) % 5 != 0:
        for j in range(p + 1, r + 1):
            if A[p] > A[j]:
                temp = A[p]
                A[p] = A[j]
                A[j] = temp

        if i == 1:
            return A[p]

        p = p + 1
        i = i - 1

    # Number of 5-element groups
    g = (r - p + 1) // 5

    # Sort each group of 5 elements using Python's built-in sort
    for j in range(p, p + g):
        group = [A[j], A[j + g], A[j + 2 * g], A[j + 3 * g], A[j + 4 * g]]
        group.sort()

        A[j] = group[0]
        A[j + g] = group[1]
        A[j + 2 * g] = group[2]
        A[j + 3 * g] = group[3]
        A[j + 4 * g] = group[4]

    # Recursively find the median of the group medians
    x = select_helper(A, p + 2 * g, p + 3 * g - 1, math.ceil(g / 2))

    # Partition around x and recurse on the side that holds rank i
    q = partition_around(A, p, r, x)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return select_helper(A, p, q - 1, i)
    else:
        return select_helper(A, q + 1, r, i - k)


def make_pairs(arr):
    """
    Convert each number arr[index] into a (value, index) pair.
    Follows CLRS Chapter 9 Footnote 1 so duplicate values are treated as distinct.
    """
    paired = []
    for index in range(len(arr)):
        paired.append((arr[index], index))
    return paired


def randomized_select(arr, k):
    """Find the k-th smallest element (1-based) using Randomized Quickselect."""
    if len(arr) == 0 or k < 1 or k > len(arr):
        raise ValueError("Array must be non-empty and k must be between 1 and len(arr).")

    paired = make_pairs(arr)
    answer_pair = randomized_select_helper(paired, 0, len(paired) - 1, k)
    return answer_pair[0]


def deterministic_select(arr, k):
    """Find the k-th smallest element (1-based) using Median of Medians (SELECT)."""
    if len(arr) == 0 or k < 1 or k > len(arr):
        raise ValueError("Array must be non-empty and k must be between 1 and len(arr).")

    paired = make_pairs(arr)
    answer_pair = select_helper(paired, 0, len(paired) - 1, k)
    return answer_pair[0]


# Quick test you can run right away
if __name__ == "__main__":
    sample = [12, 3, 5, 7, 3, 19, 5]
    k = 4  # Looking for the 4th smallest element (which is 5)
    print("Randomized Select:", randomized_select(sample, k))
    print("Deterministic Select:", deterministic_select(sample, k))
