from core.sudoku import Sudoku 
from core.cell import Cell
from core.unit import Unit
from collections.abc import Iterable
from itertools import combinations

# ---------------- Techniques ----------------
def naked_single(sudoku:Sudoku):
    
    """A cell has only one remaining possible candidate after eliminating
    the numbers already present in its row, column, and box.
    This candidate must therefore be the value of the cell."""
    
    for cell in sudoku.cells:
        if not cell.is_solved:
            cell.reduce_candidates()

            if len(cell.candidates) == 1:
                cell.solve(cell.candidates.pop())
                return True
    return False


def hidden_single(sudoku:Sudoku) -> bool:
    
    """Within a unit (row, column, or box), a digit can only be placed
    in a single cell, even if that cell contains multiple candidates.
    All other candidates are removed from this cell and the value is fixed."""

    for unit in sudoku.units:

        for i in range(1,10):
            cells_with_candidate = unit.get_cells_with_candidates(i)
            if len(cells_with_candidate) == 1:
                cells_with_candidate[0].solve(i)

                return True
            
    return False


def pointing_candidates(sudoku:Sudoku) -> bool:
    
    """Within a box, all candidates of a given digit are confined to a
    single row or a single column.
    That digit can therefore be eliminated from all other cells in that
    row or column outside the box."""

    for box_id, box in sudoku.boxes.items():

        for candidate in range(1,10):
            if candidate in box.values:
                continue
            
            for attr in ("rows", "cols"):

                concerned_rows_cols= box.candidate_in(attr, candidate)

                if len(concerned_rows_cols) != 1:
                    continue

                unit_to_check = concerned_rows_cols.pop()

                for cell in getattr(sudoku, attr)[unit_to_check]:
                    if cell.box == box_id:
                        continue

                    if cell.remove_candidates(candidate):
                        return True
    
    return False


def claiming_candidates(sudoku:Sudoku) -> bool:
    
    """Within a row or a column, all candidates of a given digit are restricted
    to a single box. That digit can then be removed from the other cells of that box."""
    
    for unit in sudoku.units:

        if not unit.is_line:
            continue

        for candidate in range(1,10):

            in_boxes = unit.candidate_in("boxes", candidate)

            if len(in_boxes) == 1:
                box_id = in_boxes.pop()

                for cell in sudoku.boxes[box_id]:
                    if getattr(cell, unit.unit_type) != unit.unit_id:
                        if cell.remove_candidates(candidate):
                            return True

    return False

                
def naked_subset(sudoku: Sudoku) -> bool:

    "Two/three/fours cells in the same unit contain exactly the same two/three/four candidates"
    "These digits must occupy these cells"
    "They can be removed from the other cell's candidate inside the unit"

    for size in range(2,5): #naked pair, triple and quadruple

        for unit in sudoku.units:
            
            #filter out empty sets and too long candidates lists to lighten the combination process
            comparable_cells = [cell for cell in unit 
                                if 1 < len(cell.candidates) <= size] 

            for comb in combinations(comparable_cells, size):

                candidates = set().union(
                    *(cell.candidates for cell in comb)) #flatten the candidates

                if len(candidates) != size: #not a naked subset
                    continue

                for unit_cell in unit.get_cells(excluded=comb):
                    if unit_cell.remove_candidates(candidates):
                        return True
    
    return False


def hidden_subset(sudoku: Sudoku) -> bool:

    for size in range(2,5):

        for unit in sudoku.units:

                comparable_cells = [cell for cell in unit if cell.candidates]
                candidates = set().union(*(unit.candidates))

                for comb in combinations(candidates, size):
                        
                        comb = set(comb)
                        cells_with_cand = [c for c in comparable_cells 
                                        if any(cand in comb 
                                        for cand in c.candidates)]

                        
                        if len(cells_with_cand) != size:
                            continue
                        
                        for c in cells_with_cand:
                            to_be_eliminated = set(c.candidates) - comb
                            if c.remove_candidates(to_be_eliminated):
                                return True

    return False
