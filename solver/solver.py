from core.sudoku import Sudoku
from .techniques.level_1_basics import *
from .techniques.level_2_intermediate import *

def solve(sudoku: Sudoku):

    techniques = [naked_single, hidden_single, pointing_candidates, claiming_candidates, naked_subset, hidden_subset, 
                  x_wing]
    progress = True


    while progress:
        progress = False
        
        sudoku.check_status()
        for technique in techniques:
            print (technique.__name__)
            
            if technique(sudoku):
                print("_________________", technique.__name__, "_________________")
                sudoku.refresh()
                progress = True
                break
            
            if sudoku.is_solved:
                return sudoku
