from cell import Cell

class Unit:
    def __init__(self, unit_type:str, unit_id:int, cells: list[Cell]):
        self.unit_id = unit_id
        self.unit_type = unit_type
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)

    def __repr__(self):
            identity = f"{str(self.unit_type)} : {str(self.unit_id)}"
            values = f"Values (list[int]) : {' - '.join([str(v) for v in self.values])}"
            candidates = f"Candidates (list[set]) : {' | '.join([str(cand) for cand in self.candidates])}"
            return "\n".join([identity, values, candidates])
    
# ---------------- values ----------------

    @property
    def values(self) -> list[int]:
        return [cell.value for cell in self.cells if cell.value is not None]
    
# ---------------- candidates ----------------

    @property
    def candidates(self) -> list[set[int]]:
        return [cell.candidates for cell in self.cells]
    
    def get_cells(self, excluded=None):
         # same as candidate property but may exclude specific cells
         if excluded is None:
              return self.cells
         
         if isinstance(excluded, Cell):
              excluded = {excluded}

         return [cell for cell in self.cells if cell not in excluded]

    def get_cells_with_candidates(self, candidate:int) -> list[Cell]:
        return [cell for cell in self.cells if candidate in cell.candidates]
    
    def candidate_in(self, unit_type:str, candidate:int) -> set[int]:
         if unit_type == "rows":
              return set([c.row for c in self.cells if candidate in c.candidates])
         if unit_type == "cols":
              return set([c.col for c in self.cells if candidate in c.candidates])
         if unit_type == "boxes":
              return set([c.box for c in self.cells if candidate in c.candidates])
         
    def candidates_counter(self)->dict[int:int]:
         return {i:len([c for c in self.cells if i in c.candidates]) for i in range(1,10)}
    
    def get_candidate_cells(self, candidate:int)->list[Cell]:
         return [cell for cell in self.cells if candidate in cell.candidates]
         
         


# ---------------- indexing ----------------
    
    @property
    def get_concerned_units(self) -> dict:
            concerned_rows = set([c.row for c in self.cells])
            concerned_cols = set([c.col for c in self.cells])
            concerned_boxes = set([c.box for c in self.cells])

            return {"rows": concerned_rows,
                    "cols": concerned_cols,
                    "boxes": concerned_boxes
                    }
    
# ---------------- status ----------------

    @property
    def is_line(self) -> bool:
        return self.unit_type in ("row", "col")

    @property
    def is_solved(self) -> bool:
        if len(self.values) != 9:
            return False
        
        if set(self.values) != set(range(1,10)):
            raise ValueError(f"Invalid {self.unit_type} {self.unit_id} : {self.values}")
            
        return True
    
    def check(self) -> bool:
        values = self.values
        return len(values) == len(set(values))



if __name__ == "__main__":
    from loader import loader

    sudoku = loader()
    unit = Unit("row", 1, sudoku.rows[1])
    print(unit.candidates_counter())