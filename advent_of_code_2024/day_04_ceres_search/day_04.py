import numpy as np
import re
from numpy import ndarray


def parse_input():
    with open("input.txt") as fh:
        wordsearch = [list(line.strip()) for line in fh.readlines()]
    return wordsearch


class WordSearch:
    def __init__(self, wordsearch):
        self.ws = np.array(wordsearch)
        self.cols, self.rows = self.ws.shape
        self.regex = re.compile(r"XMAS")

    def rows_cols(self, ws):
        lines = []
        for x in ws:
            line = "".join(x)
            lines += [line, line[::-1]]
        return lines

    def diagonals(self, ws):
        lines = []
        for offset in range(-1 * (self.rows - 1), self.cols):
            line = "".join(np.diagonal(ws, offset))
            lines += [line, line[::-1]]
        return lines

    @property
    def lines(self):
        return (
            self.rows_cols(self.ws)
            + self.rows_cols(self.ws.T)
            + self.diagonals(self.ws)
            + self.diagonals(np.fliplr(self.ws))
        )

    def is_mas(self, tile: ndarray):
        index = np.array([0, 2, 4, 6, 8])
        tile = tile.ravel()
        tile = "".join(tile[index])
        return tile in ["SSAMM", "MSAMS", "MMASS", "SMASM"]

    def part_1(self):
        total = 0
        for line in self.lines:
            matches: list[str] = self.regex.findall(line)
            total += len(matches)
        return total

    def part_2(self):
        total = 0
        for i in range(self.rows - 2):
            for j in range(self.cols - 2):
                tile = self.ws[i : i + 3, j : j + 3]
                if self.is_mas(tile):
                    total += 1
        return total


if __name__ == "__main__":
    wordsearch = parse_input()
    ws = WordSearch(wordsearch)
    print(ws.part_1())
    print(ws.part_2())
