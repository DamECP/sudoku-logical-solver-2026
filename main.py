from solver.solver import solve
from solver.loader import loader

def main():
    path = "data/sudokus/test_xwing.txt"

    sudoku = loader(path)
    solve(sudoku)

    print(sudoku)


if __name__ == "__main__":
    main()