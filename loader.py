from sudoku import Sudoku

PATH = "test_hard.txt"
def loader(path=PATH) -> Sudoku:
    with open(path, "r") as s:
        s = [i.strip() for i in s.readlines()][0:10] # tests individuels
        s = Sudoku(s)
        s.build()
        s.build_peers()
        return s


if __name__ == "__main__":
    sudoku = loader()
    print(sudoku)