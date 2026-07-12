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

    def unit_candidates(self, unit_type:str, candidate:int) -> list[Cell]:
        if unit_type == "unit":
            return [cell for cell in self.cells if candidate in cell.candidates]
        elif unit_type == "row":
            return [c.row for c in self.cells if candidate in c.candidates]    
        elif unit_type == "col":
            return [c.col for c in self.cells if candidate in c.candidates]
    
    def count_candidates(self) -> dict[int: list[Cell]]:
        cells = [c for c in self.cells if c.candidates]
        return {i: [c for c in cells if i in c.candidates] for i in range(1,10)}


# ---------------- indexing ----------------
    
    @property
    def concerned_rows(self, candidate) -> set[int]:
        return set([c.row for c in self.cells])
    
    @property
    def concerned_cols(self) -> set[int]:
        return set([c.col for c in self.cells])
    
    @property
    def concerned_boxes(self) -> set[int]:
        return set([c.box for c in self.cells])

    
# ---------------- status ----------------

    @property
    def is_line(self) -> bool:
        return self.unit_type in ("row", "col")

    @property
    def is_finished(self) -> bool:
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
    print(unit)