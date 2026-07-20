from cell import Cell
from unit import Unit

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.rows: dict[int, list[Cell]] = {i: Unit("row", i, []) for i in range(1,10)}
        self.cols: dict[int: list[Cell]] = {i: Unit("col", i , []) for i in range(1,10)}
        self.boxes: dict[int: list[Cell]] = {i: Unit("box", i, []) for i in range(1,10)}
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

                self.rows[i].cells.append(c)
                self.cols[j].cells.append(c)
                self.boxes[current_box].cells.append(c)
                self.dictionary[(i,j)] = c
                self.cells.append(c)
                cell_id+=1
            
            

    def build_peers(self) -> None:
        for c in self.cells:
            c.row_peers = [i for i in self.rows[c.row].cells if i is not c]
            c.col_peers = [i for i in self.cols[c.col].cells if i is not c]
            c.box_peers = [i for i in self.boxes[c.box].cells if i is not c]
            c.peers = set(c.row_peers + c.col_peers + c.box_peers)

    def check_status(self) -> bool:
        
        for unit in self.units:
            if not unit.check():
                raise Exception(f"Incoherence : {unit}")

        return True
    

    def update_candidates(self) -> None:
        for cell in self.cells:
            cell.reduce_candidates()


    def refresh(self) -> None:
        self.update_candidates()
        self.check_status()

    def get_cell(self, x, y) -> Cell:
        return self.dictionary[(x,y)]
    
                
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
    from loader import loader

    sudoku = loader()
    sudoku.check_status()