from cell import Cell

class Unit:
    def __init__(self, unit_type:str, unit_id:int, cells: list[Cell]):
        self.unit_id = unit_id
        self.unit_type = unit_type
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)

    @property
    def values(self) -> list:
        return [cell.value for cell in self.cells if cell.value is not None]
    
    @property
    def candidates(self) -> list:
        return [cell.candidates for cell in self.cells]
    
    @property
    def candidates_counter(self) -> dict[int: list[Cell]]:
        cells = [c for c in self.cells if c.candidates]
        return {i: [c for c in cells if i in c.candidates] for i in range(1,10)}
    
    @property
    def is_finished(self):
        if len(self.values) != 9:
            return False
        
        if set(self.values) != set(range(1,10)):
            raise ValueError(f"Invalid {self.type} {self.id} : {self.values}")
            
        return True


if __name__ == "__main__":
    from loader import loader

    sudoku = loader()
    unit = Unit("row", 1, sudoku.rows[1])
    print(unit.candidates)