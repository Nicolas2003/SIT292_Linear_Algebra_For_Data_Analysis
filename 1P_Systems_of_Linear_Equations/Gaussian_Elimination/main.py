def gaussian_elimination(matrix):
    matrix_size = len(matrix)

    for main_row in matrix:
        column = matrix[main_row]
        choose_pivot = False
        chosen_multiple = False
        m = None
        a = None

        for elements in range(0, len(column)):
            if column[elements] != 0 and not choose_pivot:
                a = column[elements]
                choose_pivot = True

            for i in range(0, len(column)):
                if choose_pivot:
                    column[i] = (1 / a) * column[i]

        for row in range(1, matrix_size):
            for i in range(0, len(column[row])):
                if column[row][i] != 0 and not chosen_multiple:
                    m = column[row][i]
                    chosen_multiple = True

            for column_position in range(0, len(column[row])):
                if chosen_multiple:
                    column[row][column_position] = column[row][column_position] - m * column[row][column_position]

    return matrix

matrix = {0: [-1, 3, 1, 3, 2, 1],
          1: [-2, 6, 1, -5, 0, -1],
          2: [3, -9, 2, 4, 1, -1],
          3: [1, -3, -1, 3, 0, 1]}

result = gaussian_elimination(matrix)


