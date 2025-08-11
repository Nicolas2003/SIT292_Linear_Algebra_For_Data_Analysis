def solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"rows: {rows}, cols: {cols}")

    for main_row in range(0, rows):
        # print(matrix)
        # find the next pivot
        pivot = None
        for col in range(0, cols - 1):
            if matrix[main_row][col] != 0:
                pivot = col
                break
        if pivot is None:
            continue
        print(f"main_row: {main_row}, pivot: {pivot}")

        # make the value in pivot = 1
        unifying_factor = 1 / matrix[main_row][pivot]
        for col in range(0, cols):
            matrix[main_row][col] *= unifying_factor

        print("unify pivot column")
        print_matrix(matrix)

        # make the values in pivot = 0
        for row in range(0, rows):
            if row != main_row:
                eliminating_factor = matrix[row][pivot]
                for col in range(0, cols):
                    matrix[row][col] -= (eliminating_factor * matrix[main_row][col])

        print("zero pivot column")
        print_matrix(matrix)


def print_matrix(matrix):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            print(f"{matrix[row][col]}", end = ' ')
        print()
    print()


matrix = [
    [ 3, 8, -3, -14, 2],
    [ 2, 3, -1, -2, 1],
    [ 1, -2, 1, 10, 0],
    [ 1, 5, -2, -12, 1]
]


def main():
    solve(matrix)
    print_matrix(matrix)

if __name__ == '__main__':
    main()
