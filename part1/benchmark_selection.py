import random
import time
from selection import deterministic_select, randomized_select


def run_tests():
    """Test both algorithms against Python's built-in sorted() on edge cases."""
    test_lists = [
        [42],                        # Single element
        [5, 5, 5, 5, 5],             # All duplicates
        [3, 1, 2, 1, 3, 2, 1],       # Many duplicates
        [-10, 0, -5, 12, 7, 3],      # Negative numbers
        [1, 2, 3, 4, 5, 6, 7],       # Already sorted
        [7, 6, 5, 4, 3, 2, 1],       # Reverse sorted
    ]

    for arr in test_lists:
        sorted_arr = sorted(arr)
        for k in range(1, len(arr) + 1):
            expected = sorted_arr[k - 1]
            r_result = randomized_select(arr, k)
            d_result = deterministic_select(arr, k)

            if r_result != expected or d_result != expected:
                print("Test failed on:", arr, "for k =", k)
                return

    print("All correctness and edge-case tests passed!\n")


def make_dataset(size, dist_type):
    """Create a test list of the given size and distribution."""
    if dist_type == "random":
        data = []
        for _ in range(size):
            data.append(random.randint(1, size * 10))
        return data
    elif dist_type == "sorted":
        return list(range(size))
    elif dist_type == "reverse_sorted":
        return list(range(size, 0, -1))
    elif dist_type == "duplicates":
        data = []
        for _ in range(size):
            data.append(random.randint(1, 10))
        return data


def measure_average_ms(func, data, k, trials):
    """Run func multiple times and return the average runtime in milliseconds."""
    total_time = 0.0
    for _ in range(trials):
        start = time.perf_counter()
        func(data, k)
        end = time.perf_counter()
        total_time = total_time + (end - start)

    avg_seconds = total_time / trials
    return avg_seconds * 1000


def run_benchmarks():
    """Compare runtimes across different array sizes and distributions."""
    sizes = [1000, 5000, 10000, 20000]
    distributions = ["random", "sorted", "reverse_sorted", "duplicates"]
    trials = 3

    print("Distribution    | Size   | Randomized (ms) | Deterministic (ms)")
    print("---------------------------------------------------------------")

    for dist in distributions:
        for size in sizes:
            random.seed(42)  # Keeps the generated data repeatable
            data = make_dataset(size, dist)
            k = (size + 1) // 2  # Lower median

            rand_ms = measure_average_ms(randomized_select, data, k, trials)
            det_ms = measure_average_ms(deterministic_select, data, k, trials)

            print(f"{dist:<15} | {size:<6} | {rand_ms:<15.3f} | {det_ms:<18.3f}")
        print("---------------------------------------------------------------")


if __name__ == "__main__":
    run_tests()
    run_benchmarks()
