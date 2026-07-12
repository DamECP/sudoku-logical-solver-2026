from sudoku import Sudoku 
from cell import Cell
from unit import Unit
from collections.abc import Iterable


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
            cells_with_candidate = unit.unit_candidates("unit",i)
            if len(cells_with_candidate) == 1:
                cells_with_candidate[0].solve(i)

                return True
            
    return False


def pointing_candidates(sudoku:Sudoku) -> bool:
    
    """Within a box, all candidates of a given digit are confined to a
    single row or a single column.
    That digit can therefore be eliminated from all other cells in that
    row or column outside the box."""

    changes = False

    for box in sudoku.boxes.values():

        for candidate in range(1,10):
            if candidate in box:
                continue
            
            in_rows = set(box.unit_candidates("row", candidate))
            in_cols = set(box.unit_candidates("col", candidate))

            if len(in_rows) == 1:
                row_to_clean = in_rows.pop()
                for c in sudoku.rows[row_to_clean]:
                    if c.box != box.unit_id:
                        if c.remove_candidates(candidate):
                            changes = True
            
            if len(in_cols) == 1:
                col_to_clean = in_cols.pop()

                for c in sudoku.cols[col_to_clean]:
                    if c.box != box.unit_id:
                        if c.remove_candidates(candidate):
                            changes = True

    return changes


def claiming_candidates(sudoku:Sudoku) -> bool:
    
    """Within a row or a column, all candidates of a given digit are restricted
    to a single box.
    That digit can then be removed from the other cells of that box."""
    
    for unit in sudoku.units:

        if not unit.is_line:
            continue

        for candidate in range(1,10):

            pass

    
    return False

                


if __name__ == "__main__":
    from loader import loader

    sudoku = loader()
    sudoku.refresh()
    pointing_candidates(sudoku)
    #print()
    #print(sudoku)
