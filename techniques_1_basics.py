from loader import loader
from classes import * 
from collections.abc import Iterable

# ---------------- update functions ----------------
def reduce_candidates(cell:Cell) -> None:
    peers_values = {peer.value for peer in cell.peers if peer.is_solved}
    cell.candidates -= peers_values

def update_grid(sudoku:Sudoku) -> None:
    for cell in sudoku.cells:
        reduce_candidates(cell)

def remove_candidates(cells:Cell |Iterable[Cell] , candidates:int |Iterable[int]) -> None:
    if isinstance(candidates, int):
        candidates = {candidates}
    else:
        candidates = set(candidates)

    changes = False

    if isinstance(cells, Cell):
        before = cells.candidates.copy()
        cells.candidates -= candidates
        if before != cells.candidates:
            changes = True

    else:
        for cell in cells:
            before = cell.candidates.copy()
            cell.candidates -= candidates
            if before != cell.candidates:
                changes = True
    
    return changes


# ---------------- Helpers ----------------
def candidates_counter(unit: list[Cell]) -> dict[int: list[Cell]]:

    current_cells = [c for c in unit if c.candidates]
    current_candidates = {
        i:[cell for cell in current_cells if i in cell.candidates]
        for i in range(1,10)
    }

    return current_candidates


# ---------------- Techniques ----------------
def naked_single(sudoku:Sudoku):
    
    """A cell has only one remaining possible candidate after eliminating
    the numbers already present in its row, column, and box.
    This candidate must therefore be the value of the cell."""
    
    for cell in sudoku.cells:
        if not cell.is_solved:
            reduce_candidates(cell)
            if len(cell.candidates) == 1:
                cell.value = cell.candidates.pop()
                return True
    return False

def hidden_single(sudoku:Sudoku) -> bool:
    
    """Within a unit (row, column, or box), a digit can only be placed
    in a single cell, even if that cell contains multiple candidates.
    All other candidates are removed from this cell and the value is fixed."""

    for unit in sudoku.units:
        
        current_candidates = candidates_counter(unit)
            
        for candidate, candidate_count in current_candidates.items():
            if len(candidate_count) == 1:
                cell = candidate_count[0]

                cell.value = candidate
                cell.candidates.clear()

                return True
            
    return False

def pointing_candidates(sudoku:Sudoku) -> bool:
    
    """Within a box, all candidates of a given digit are confined to a
    single row or a single column.
    That digit can therefore be eliminated from all other cells in that
    row or column outside the box."""

    for box_n, box_content in sudoku.boxes.items():
        unit_candidates = candidates_counter(box_content)

        for candidate in range(1,10):
    
            in_rows = {c.row for c in unit_candidates[candidate]}
            in_cols = {c.col for c in unit_candidates[candidate]}

            if len(in_rows) == 1:
                row = in_rows.pop()
                other_cells_from_row = [c for c in sudoku.rows[row] if c.box != box_n and candidate in c.candidates]
                if len(other_cells_from_row) > 0:
                    if remove_candidates(other_cells_from_row, candidate):
                        return True
            
            if len(in_cols) == 1:
                col = in_cols.pop()
                other_cells_from_col = [c for c in sudoku.cols[col] if c.box != box_n and candidate in c.candidates]
                if len(other_cells_from_col) > 0:
                    if remove_candidates(other_cells_from_col, candidate):
                        return True
                
    return False

def claiming_candidates(sudoku:Sudoku) -> bool:
    
    """Within a row or a column, all candidates of a given digit are restricted
    to a single box.
    That digit can then be removed from the other cells of that box."""
    
    units = [sudoku.rows, sudoku.cols]

    for unit in units:

        for cells in unit.values():

            for candidate in range(1,10):

                boxes = {c.box for c in cells if candidate in c.candidates}

                if len(boxes) == 1:

                    current_box = boxes.pop()

                    for cell in sudoku.boxes[current_box]:

                        if cell not in cells and candidate in cell.candidates:
                            
                            remove_candidates(cell, candidate)
                            return True

    return False

                


if __name__ == "__main__":
    sudoku = loader()
    update_grid(sudoku)
    pointing_candidates(sudoku)
    claiming_candidates(sudoku)
    #print()
    #print(sudoku)
