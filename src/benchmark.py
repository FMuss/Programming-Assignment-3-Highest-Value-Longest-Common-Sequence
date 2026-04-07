#!/usr/bin/env python3

import random
import time
import os
import matplotlib.pyplot as plt
from lcs import lcs

TEST_SIZES = [25, 50, 100, 200, 300, 400, 500, 600, 750, 1000]


def random_instance(n, alphabet_size=4):
    chars = random.sample('abcdefghijklmnopqrstuvwxyz', alphabet_size)
    values = {}

    for c in chars:
        values[c] = random.randint(1, 10)

    A = ''.join(random.choices(chars, k=n))
    B = ''.join(random.choices(chars, k=n))

    return values, A, B


def run_benchmark():
    lcs_results = {}

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")
    os.makedirs(output_dir, exist_ok=True)

    for n in TEST_SIZES:
        values, A, B = random_instance(n)

        start = time.perf_counter()
        lcs(values, A, B)
        end = time.perf_counter()

        total_time = end - start
        lcs_results[n] = total_time
        print(f"LCS n = {n}: {total_time:.6f}s")
        
    return lcs_results


def plot(results, output_file, test):
    x_axis = []
    y_axis = []
    for n in TEST_SIZES:
        x_axis.append(n)
        y_axis.append(results[n])

    plt.figure()
    plt.plot(x_axis, y_axis)
    plt.grid(True)
    plt.xlabel("n (string length)")
    plt.ylabel("running time (s)")
    plt.title(test + " at different n")
    plt.savefig(output_file)
    plt.close()


def main():
    results = run_benchmark()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plot(results, os.path.join(project_root, "output/lcs_benchmark.png"), "LCS runtime")
    print("Saved graph to output/lcs_benchmark.png")


if __name__ == "__main__":
    main()