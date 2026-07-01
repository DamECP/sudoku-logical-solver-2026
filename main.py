from sudoku import Sudoku

def main():
    with open("sudoku_test_1.txt", "r") as s:
        s = [i.strip() for i in s.readlines()]
        s = Sudoku(s)
        s.build()
        s.build_peers()
        return s

main()

if __name__ == "__main__":
    sudoku = main()
    for i in sudoku.cells.values():
        print(i)
        print()