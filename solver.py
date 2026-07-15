from loader import loader
from sudoku import Sudoku
from techniques_1_basics import *

sudoku = loader()
print(sudoku)
print()

techniques = [naked_single, hidden_single, pointing_candidates, claiming_candidates, naked_subset]
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


print(sudoku)
