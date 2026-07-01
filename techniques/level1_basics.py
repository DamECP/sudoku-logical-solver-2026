import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from sudoku import Sudoku

def naked_single(sudoku: Sudoku) -> bool:
    progress = False

    for cell in sudoku.cells.values():

        if not cell.value:

            for peer in cell.peers:
                if peer.value in cell.candidates:
                    cell.candidates.remove(peer.value)
                    progress = True

            if len(cell.candidates) == 1:
                cell.value = next(iter(cell.candidates))
                cell.candidates.clear()
                progress = True

    return progress

                    

    
if __name__ == "__main__":

    with open("sudoku_test_1.txt", "r") as s:
        s = [i.strip() for i in s.readlines()]
        s = Sudoku(s)
        s.build()
        s.build_peers()
        
        naked_single(s)