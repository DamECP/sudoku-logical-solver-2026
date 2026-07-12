from loader import loader
from sudoku import Sudoku
from techniques_1_basics import *

sudoku = loader()
print(sudoku)
print()

techniques = [naked_single, hidden_single, pointing_candidates, claiming_candidates]
progress = True


while progress:
    progress = False
    
    sudoku.check_status()
    for technique in techniques:
        
        if technique(sudoku):
            print(technique.__name__)
            sudoku.refresh()
            
            progress = True
            break


print(sudoku)
