#!/usr/bin/env python3
import sys
import os


def lcs(values, A, B):
    m = len(A)
    n = len(B)

    # Fill data structure
    best_val = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                # Chars match
                best_val[i][j] = best_val[i-1][j-1] + values.get(A[i-1], 0)
            else:
                # Chars don't match
                best_val[i][j] = max(best_val[i-1][j], best_val[i][j-1])

    # Backtrack through table to make resulting string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            # Chars match, add to result
            result.append(A[i-1])
            i -= 1
            j -= 1
        elif best_val[i-1][j] >= best_val[i][j-1]:
            # Skipped char in A
            i -= 1
        else:
            # Skipped char in B
            j -= 1

    result.reverse()
    result = ''.join(result)
    return best_val[m][n], result


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 lcs.py <input_file>")
        return

    try:
        with open(sys.argv[1]) as f:
            lines = f.read().strip().splitlines()

        i = 0
        k = int(lines[i]); i += 1

        if k <= 0:
            print("Alphabet size k must be a positive integer")
            return

        values = {}
        for _ in range(k):
            char, val = lines[i].split(); i += 1
            values[char] = int(val)

        A = lines[i]; i += 1
        B = lines[i]; i += 1

        if len(A) == 0 or len(B) == 0:
            print(0)
            print("")
            return

        max_val, result = lcs(values, A, B)

        print(max_val)
        print(result)

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(project_root, "output")
        os.makedirs(output_dir, exist_ok=True)
        input_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
        output_file = os.path.join(output_dir, input_name + ".out")
        with open(output_file, "w") as f:
            f.write(f"{max_val}\n")
            f.write(f"{result}\n")

    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except (ValueError, IndexError):
        print("Invalid input format")


if __name__ == '__main__':
    main()
