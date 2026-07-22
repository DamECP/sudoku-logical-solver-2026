from core.sudoku import Sudoku 
from core.cell import Cell
from core.unit import Unit

def x_wing(sudoku: Sudoku) -> bool:
    progress = False

    def get_corners(sudoku:Sudoku, unit:Unit, next_unit:Unit, coord1:int, coord2:int) -> list[Cell]:
        if unit.unit_type == "row":
            return [sudoku.get_cell(unit.unit_id, coord1),
                    sudoku.get_cell(unit.unit_id, coord2),
                    sudoku.get_cell(next_unit.unit_id, coord1),
                    sudoku.get_cell(next_unit.unit_id, coord2)]
        elif unit.unit_type == "col":
            return [sudoku.get_cell(coord1, unit.unit_id),
                    sudoku.get_cell(coord2, unit.unit_id),
                    sudoku.get_cell(coord1, next_unit.unit_id ),
                    sudoku.get_cell(coord2, next_unit.unit_id )]
        else:
            raise ValueError(f"Incorrect type for current unit : {unit.unit_type}")


    for units, opposite_units, opposite_attr in (
        (sudoku.rows, sudoku.cols, "col"),
        (sudoku.cols, sudoku.rows, "row")
        ):

        current_units = list(units.values())

        for candidate in range(1,10):

            for index, current_elt in enumerate(current_units):
                if candidate in current_elt.values:
                    continue

                concerned = {getattr(c, opposite_attr) for c in current_elt.get_cells_with_candidates(candidate)}

                if len(concerned) !=2:
                    continue

                for next_elt in current_units[index+1:]:

                    compared = {getattr(c, opposite_attr) for c in next_elt.get_cells_with_candidates(candidate)}

                    if compared != concerned:
                        continue

                    coord1, coord2 = concerned

                    corners = get_corners(sudoku, current_elt, next_elt, coord1, coord2)
                    targeted_cells = (opposite_units[coord1].cells + opposite_units[coord2].cells)

                    for cell in targeted_cells:
                        if cell in corners:
                            continue
                        if cell.remove_candidates(candidate):
                            progress = True
    
    return progress