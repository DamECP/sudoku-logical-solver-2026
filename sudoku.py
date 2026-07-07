from typing import List, Dict
from cell import Cell

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.rows: dict[int:Cell] = {i: [] for i in range(1,10)}
        self.cols: dict[int:Cell] = {i: [] for i in range(1,10)}
        self.boxes: dict[int:Cell] = {i: [] for i in range(1,10)}
        self.dictionary = {}
        self.cells: list[Cell] = []
        self.units = [*self.rows.values(), *self.cols.values(), *self.boxes.values()]

    def build(self):
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

    def build_peers(self):
        for c in self.cells:
            c.row_peers = [i for i in self.rows[c.row] if i is not c]
            c.col_peers = [i for i in self.cols[c.col] if i is not c]
            c.box_peers = [i for i in self.boxes[c.box] if i is not c]
            c.peers = set(c.row_peers + c.col_peers + c.box_peers)

    def check_status(self):
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
    with open("sudoku_test_1.txt", "r") as s:
        s = [i.strip() for i in s.readlines()]

    s = Sudoku(s)
    s.build()
    print(s)
