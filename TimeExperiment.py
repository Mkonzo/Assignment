"""
Task 3: Timing experiment
Measure sum() for 1,000 to 16,000 items, doubling the size each
time, to observe how runtime scales with input size (n).
"""

import timeit


def measure_sum_time(n, repeats=1000):
    data = list(range(n))
    total_time = timeit.timeit(lambda: sum(data), number=repeats)
    return total_time / repeats     # average time per call, in seconds


if __name__ == "__main__":
    sizes = [1000, 2000, 4000, 8000, 16000]

    print(f"{'n':>8} | {'avg time (s)':>14} | {'time / n':>12}")
    print("-" * 40)
    for n in sizes:
        avg_time = measure_sum_time(n)
        print(f"{n:>8} | {avg_time:>14.8f} | {avg_time/n:>12.10f}")