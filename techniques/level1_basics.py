import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sudoku import Sudoku

def reduce_candidates(sudoku: Sudoku) -> bool:
    """Checks for peers (in rows, cols and boxes)
    and reduce the cells' candidates"""
    progress = False

    for cell in sudoku.cells.values():

        if not cell.is_solved:

            for peer in cell.peers:
                if peer.value in cell.candidates:
                    cell.candidates.remove(peer.value)
                    progress = True
    
    return progress


def sole_candidate(sudoku:Sudoku) -> bool:

    progress = False

    for cell in sudoku.cells.values():

            if len(cell.candidates) == 1:
                cell.value = next(iter(cell.candidates))
                cell.candidates.clear()
                progress = True
        
    return progress



    
if __name__ == "__main__":

    with open("../sudoku_test_1.txt", "r") as s:
        s = [i.strip() for i in s.readlines()]
        s = Sudoku(s)
        s.build()
        s.build_peers()
        
        print(s)
        print()
            
        print()
        reduce_candidates(s)
        print(s)
