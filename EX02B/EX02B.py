"""Conversion from row, col => cell index and vice versa."""


def get_cell_index(row, col, row_len):
    return row * row_len + col


def get_row_and_col(cell_index, row_len):
    return cell_index // row_len, cell_index - cell_index // row_len * row_len


def get_row_len(row, col, cell_index):
    return (cell_index - col) // row if (cell_index - col) // row >= col else -1


if __name__ == '__main__':
    print(get_cell_index(0, 3, 10))  # => 3
    print(get_cell_index(0, 0, 10))  # => 0
    print(get_cell_index(11, 12, 13))  # => 155

    print(get_row_and_col(3, 2))  # => (1, 1)
    print(get_row_and_col(2, 3))  # => (0, 2)
    print(get_row_and_col(123, 17))  # => (7, 4)

    print(get_row_len(1, 3, 4))  # => -1
    print(get_row_len(1, 0, 3))  # => 3
    print(get_row_len(12, 0, 12))  # => 1
