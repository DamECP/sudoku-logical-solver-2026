from classes import *
from techniques_1_basics import *

sudoku = loader()
print(sudoku)
print()

runs = 1
techniques = [naked_single, hidden_single, pointing_candidates, claiming_candidates]
progress = True


while progress:
    progress = False
    
    sudoku.check_status()
    for technique in techniques:
        
        if technique(sudoku):
            update_grid(sudoku)
            sudoku.check_status()
            
            progress = True
            break


print(sudoku)
