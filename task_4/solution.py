import sys
from pprint import pprint
from dataclasses import dataclass


def parse_boards(boards):
    b = []
    with open(boards) as f:
        tmp = []
        for line in f:
            if line.startswith("\n"):
                tmp1 = tmp[::]
                tmp.clear()
                b.append(tmp1)
            else:
                tmp.append(list(map(int, line.strip().split())))
    return b


def build_cells(x):
    a = []
    for idy, row in enumerate(x):
        for idx, column in enumerate(row):
            my_row = tuple([i for i in range(len(row)) if i != idx])
            my_column = tuple([i for i in range(len(x)) if i != idy])
            a.append(
                Cell(
                    x=idx, y=idy, value=column, row=my_row, column=my_column, seen=False
                )
            )
    return a


@dataclass
class Cell:
    x: int
    y: int
    row: tuple
    column: tuple
    value: int
    seen: bool


class Board:
    def __init__(self, cells: list[Cell]):
        self.cells = cells

    def __repr__(self):
        return f"{self.cells}"

    def __getitem__(self, key):
        return self.cells[key]

    def sum_unchecked(self):
        return sum(c.value for c in self.cells if not c.seen)

    def complete_neighbors(self, cell: Cell):
        neighbors_in_row = []
        neighbors_in_column = []
        for ocell in self.cells:
            if ocell.y == cell.y and ocell.x in cell.row:
                neighbors_in_row.append(ocell.seen)
            if ocell.x == cell.x and ocell.y in cell.column:
                neighbors_in_column.append(ocell.seen)
        return True if all(neighbors_in_row) or all(neighbors_in_column) else False

    def solve(self, num):
        for cell in self.cells:
            if cell.value == num:
                cell.seen = True
                s = self.sum_unchecked()
                if self.complete_neighbors(cell):
                    return s, num
        return False


def main(seq, boards):
    with open(seq) as f:
        nums = list(map(int, f.read().split(",")))
    raw_boards = parse_boards(boards)
    boards = [Board(build_cells(raw_board)) for raw_board in raw_boards]
    d = {}
    for idn, num in enumerate(nums):
        for idx, board in enumerate(boards):
            res = board.solve(num)
            if res:
                res = res + (idn,)
                if not d.get(idx):
                    d[idx] = res

    a = d.items()
    winning_board = min(a, key=lambda x: x[1][2])[1]
    sum_unchecked, last_number, num_idx = winning_board
    print(
        f"{winning_board=}",
        f"{sum_unchecked=}",
        f"{last_number=}",
        f"{num_idx=}",
        f"{sum_unchecked*last_number=}",
    )
    losing_board = max(a, key=lambda x: x[1][2])[1]
    sum_unchecked, last_number, num_idx = losing_board
    print(
        f"{losing_board=}",
        f"{sum_unchecked=}",
        f"{last_number=}",
        f"{num_idx=}",
        f"{sum_unchecked*last_number=}",
    )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
