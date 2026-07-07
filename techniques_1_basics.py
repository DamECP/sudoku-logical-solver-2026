from typing import List
from loader import loader
from sudoku import Sudoku
from cell import Cell

# ---------------- update functions ----------------
def reduce_candidates(cell:Cell) -> None:
    peers_values = {peer.value for peer in cell.peers if peer.is_solved}
    cell.candidates -= peers_values

def update_grid(sudoku:Sudoku) -> None:
    for cell in sudoku.cells:
        reduce_candidates(cell)

# ---------------- Helpers ----------------
def candidates_counter(unit: list[Cell]) -> dict:

    current_cells = [c for c in unit if c.candidates]
    current_candidates = {
        i:[cell for cell in current_cells if i in cell.candidates]
        for i in range(1,10)
    }

    return current_candidates


# ---------------- Techniques ----------------
def naked_single(sudoku:Sudoku):
    for cell in sudoku.cells:
        if not cell.is_solved:
            reduce_candidates(cell)
            if len(cell.candidates) == 1:
                cell.value = cell.candidates.pop()
                return True
    return False

def hidden_single(sudoku:Sudoku) -> bool:

    for unit in sudoku.units:
        
        current_candidates = candidates_counter(unit)
            
        for candidate, candidate_count in current_candidates.items():
            if len(candidate_count) == 1:
                cell = candidate_count[0]

                cell.value = candidate
                cell.candidates.clear()

                return True
            
    return False
                


if __name__ == "__main__":
    sudoku = loader()
    update_grid(sudoku)
    hidden_single(sudoku)

