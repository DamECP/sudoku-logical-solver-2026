from core.sudoku import Sudoku

def loader(path) -> Sudoku:
    with open(path, "r") as s:
        lines = [i.strip() for i in s.readlines()][0:10] # tests individuels
        
        sudoku = Sudoku(lines)
        sudoku.build()
        sudoku.build_peers()
        return sudoku