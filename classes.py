from typing import List, Dict

class Cell:
    def __init__(self, cell_id, value, row, col, box):
        self.id = cell_id
        self.value = value
        self.row = row
        self.col = col
        self.box = box
        self.row_peers = None
        self.col_peers = None
        self.box_peers = None
        self.peers = None

        #candidates initialisation
        if self.value is None:
            self.candidates = set(range(1,10))
        else:
            self.candidates = set()

    @property
    def is_solved(self):
        return self.value is not None
    
    def __repr__(self):
        candidates = sorted(self.candidates) if self.candidates is not None else "None"

        data = [f"id = {str(self.id)}",
                f"value = {str(self.value)}",
                f"candidates = {candidates}",
                f"row = {str(self.row)}",
                f"column = {str(self.col)}",
                f"box = {str(self.box)}",
                ]

        return "\n".join(i for i in data)

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.rows: dict[int, list[Cell]] = {i: [] for i in range(1,10)}
        self.cols: dict[int: list[Cell]] = {i: [] for i in range(1,10)}
        self.boxes: dict[int: list[Cell]] = {i: [] for i in range(1,10)}
        self.dictionary = {}
        self.cells: list[Cell] = []
        self.units = [*self.rows.values(), *self.cols.values(), *self.boxes.values()]

    def build(self) -> None:
        cell_id = 1
        for i, line in enumerate(self.sudoku, 1):
            for j, value in enumerate(line, 1):
                current_box = 3 * ((i-1) // 3) + ((j-1) // 3) + 1

                if value in "123456789":
                    value = int(value)
                else:
                    value = None
                    
                c = Cell(cell_id, value, i, j, current_box)

                self.rows[i].append(c)
                self.cols[j].append(c)
                self.boxes[current_box].append(c)
                self.dictionary[(i,j)] = c
                self.cells.append(c)
                cell_id+=1

    def build_peers(self) -> None:
        for c in self.cells:
            c.row_peers = [i for i in self.rows[c.row] if i is not c]
            c.col_peers = [i for i in self.cols[c.col] if i is not c]
            c.box_peers = [i for i in self.boxes[c.box] if i is not c]
            c.peers = set(c.row_peers + c.col_peers + c.box_peers)

    def check_status(self) -> bool:
        units = [self.rows, self.cols, self.boxes]
        for unit in units:
            for sub_unit in unit.values():
                cells_values = [cell.value for cell in sub_unit if cell.value is not None]
                if any(cells_values.count(i)>1 for i in range(1,10)):
                    raise Exception(f"Incoherence : {cells_values}")
        return True
                
    def __repr__(self):
        data = []
        def set_value(v):
            return str(v) if v is not None else "·"

        for rows in range(1,10):
            row = []

            for cells in range(1,10):
                current_cell = self.dictionary[rows,cells]
                val = set_value(current_cell.value)
                row.append(val)
                if cells in (3,6):
                    row.append("|")
            
            data.append(" ".join(row))

            if rows in (3,6):
                data.append("------|-------|------")   
        

        data = "\n".join(i for i in data)
        return data        

if __name__ == "__main__":
    test = set()
    print(bool(test))